import json
import socket
import threading
import sqlite3
import time
global noms,noms1
clients =[]
names =[]
namees=[]
server_ip = socket.gethostbyname(socket.gethostname())
servire_port = 12345
formatt = "utf-8"
servire = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servire.bind((server_ip, servire_port))
servire.listen()


def sendlistttte(message,name1):
    for client in clients:
        index = clients.index(client)
        name = names[index]
        if name==name1:
            client.send(message.encode(formatt))

def broadcast2(message,namet):
    global noms,noms1
    if message=="join the groupe":
        for client in clients:
            index = clients.index(client)
            name = names[index]
            if name==namet:
                for nom in noms:
                    client.send(f"you add {nom} to group/group".encode(formatt))
            for nom in noms:
                if nom ==name:
                    client.send(f"you add by {namet} to group/group".encode(formatt))
                elif nom !=namet and name!=namet and name in namees:
                    client.send(f"{nom} add by {namet} to group/group".encode(formatt))

    else:
        for client in clients:
            index = clients.index(client)
            name = names[index]
            if message == "join the group":
                if namet == name and name in noms1:
                    client.send(f"you created a group/group".encode(formatt))
                if namet != name and name in noms1:
                    client.send(f"you add by {namet} to group/group".encode(formatt))
            else:
                if name in namees :
                    client.send(message.encode(formatt))
def broadcast1(message,na):
    for client in clients:
        index = clients.index(client)
        name = names[index]
        if name==na:
            client.send(message.encode(formatt))
def envoyer_message(messs,nom):
    for client in clients:
        index = clients.index(client)
        name = names[index]
        if name==nom:
            client.send(messs.encode(formatt))
def unicast(message, nam, namet):
    for client in clients:
        index = clients.index(client)
        name = names[index]
        messag = f"{namet}:{message}\n"
        if nam == name:
            client.send(messag.encode(formatt))
def handle_client(client):
    global noms,noms1
    while True:
        try:
            mydata=sqlite3.connect("MyData1.db ")
            mycursor=mydata.cursor()
            mycursor.execute("CREATE TABLE IF NOT EXISTS messager_groupe(message text)")
            mycursor.execute("CREATE TABLE IF NOT EXISTS messages (nomemetteur VARCHAR(30),nomdestination VARCHAR(30),message text)")
            message = client.recv(1024).decode(formatt)
            lisst=message.split(sep="!")
            index = clients.index(client)
            nameemetteur=names[index]
            listt=message.split(sep="/")
            lll=message.split(sep="@")
            if len(lisst)==2:
                mycursor.execute("UPDATE client SET nom=? WHERE nom=?",(lisst[0],nameemetteur))
                index=clients.index(client)
                names[index]=lisst[0]
                mycursor.execute("UPDATE messages SET nomemetteur=? WHERE nomemetteur=?",(lisst[0],nameemetteur))
                mycursor.execute("UPDATE messages SET nomdestination=? WHERE nomdestination=?", (lisst[0], nameemetteur))
                message=f"{nameemetteur} change son nom par {lisst[0]}\n"
                broadcast2(message,nameemetteur)
            elif len(lll)==2:
                noms1=[]
                message=json.loads(lll[0])
                noms1=message
                for nom in message:
                    namees.append(nom)
                    envoyer_message(f"ADDgroup/{nameemetteur}/21/group/hfh",nom)
                messagez="join the group"
                broadcast2(messagez, nameemetteur)
            elif len(lll)==3:
                noms= json.loads(lll[0])
                for nom in noms:
                    namees.append(nom)
                    envoyer_message(f"ADDgroup/12/21/sfgb/sfgb", nom)
                messagez = "join the groupe"
                broadcast2(messagez, nameemetteur)
            elif len(listt) == 2:
                mes = listt[0]
                namedistination = listt[1]
                unicast(mes, namedistination, nameemetteur)
                if mes!=" ":
                    mycursor.execute("INSERT INTO messages VALUES(?,?,?)", (nameemetteur, namedistination, mes))
            elif len(listt) == 1 and message != "Historique" and message != "list" and message!=" ":
                message = f"{nameemetteur}:{message}"
                mycursor.execute("INSERT INTO messager_groupe VALUES (?)", (message,))
                messaget = f"{message}/group"
                broadcast2(messaget, nameemetteur)
            elif message == "Historique":
                index = clients.index(client)
                prenom = names[index]
                coo = sqlite3.connect("MyData1.db")
                cur = coo.cursor()
                cur.execute("SELECT message FROM messager_groupe")
                les_messages = cur.fetchall()
                lesmessage=json.dumps(les_messages)
                messagefinal=f"{lesmessage}/group/historique/tout"
                envoyer_message(messagefinal, prenom)
                coo.commit()
                coo.close()
            elif len(listt)==3:
                mycursor.execute("SELECT DISTINCT nom FROM client")
                lesname=mycursor.fetchall()
                lesnom=json.dumps(lesname)
                lesfinal=f"{lesnom}/new/list"
                sendlistttte(lesfinal,nameemetteur)
                #broadcast2(lesfinal,nameemetteur)
            mydata.commit()
            mydata.close()
        except ConnectionError:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            name = names[index]
            names.remove(name)
            break
def signin(client,na):
    liss = na.split(sep="/")
    if len(liss)==4:
        coo=sqlite3.connect("MyData1.db ")
        mycur=coo.cursor()
        mycur.execute("SELECT DISTINCT nom FROM client")
        listnom = mycur.fetchall()
        noom =" "
        for nom in listnom:
            noom = f"{noom}/{nom[0]}"
        client.send(noom.encode(formatt))
        if liss[0] not in [nom[0] for nom in listnom]:
            passwordconfigure=liss[3]
            password = liss[1]
            if passwordconfigure == password:
                names.append(liss[0])
                clients.append(client)
                nom = liss[0]
                email = liss[2]
                mycur.execute("INSERT INTO client VALUES(?,?,?)", (nom, password, email))
                message = "You are connected!\n"
                broadcast1(message, nom)
        th = threading.Thread(target=handle_client, args=(client,))
        th.start()
        coo.commit()
        coo.close()
def sende(client,na):
    separ = na.split(sep="/")
    if len(separ)==2:
        conn = sqlite3.connect("MyData1.db ")
        mycur = conn.cursor()
        password2 = separ[1]
        na = separ[0]
        mycur.execute("SELECT DISTINCT nom FROM client")
        noms=mycur.fetchall()
        nnom =" "
        for nom in noms:
            nnom = f"{nnom}/{nom[0]}"
        client.send(nnom.encode(formatt))
        row = nnom.split(sep='/')
        if na in row:
            mycur.execute("SELECT password FROM client WHERE nom=?", (na,))
            passsword = mycur.fetchall()
            password1 = passsword[0]
            passnew = password1[0]
            client.send(passnew.encode(formatt))
            if password2==passnew:
                clients.append(client)
                names.append(na)
                mycur.execute("SELECT nomemetteur,message FROM messages WHERE nomdestination=?",(na,))
                lis = mycur.fetchall()
                message = "You are connected!\n"
                broadcast1(message, na)
                for mes in lis:
                    messsage = f"{mes[0]}:{mes[1]}\n"
                    broadcast1(messsage, na)
                th = threading.Thread(target=handle_client, args=(client,))
                th.start()
            else:
                client.detach()
                client,addr=servire.accept()
                na=client.recv(1024).decode(formatt)
                sende(client,na)
        if na not in row:
            na=client.recv(1024).decode(formatt)
            threading.Thread(target=signin,args=(client,na)).start()
        conn.commit()
        conn .close()
def reciver():
    while True:
        client, aaddr = servire.accept()
        conn = sqlite3.connect("MyData1.db ")
        mycur = conn.cursor()
        mycur.execute("CREATE TABLE IF NOT EXISTS client (nom VARCHAR(30),password VARCHAR(30),email VARCHAR(50))")
        na= client.recv(1024).decode(formatt)
        liss=na.split(sep="/")
        if len(liss)==4:
            mycur.execute("SELECT DISTINCT nom FROM client")
            listnom=mycur.fetchall()
            noom=" "
            for nom in listnom:
                noom=f"{noom}/{nom[0]}"
            client.send(noom.encode(formatt))
            if liss[0] not in [nom[0] for nom in listnom]:
                passwordconfigure = liss[3]
                password = liss[1]
                if passwordconfigure==password:
                    nom = liss[0]
                    email = liss[2]
                    names.append(liss[0])
                    clients.append(client)
                    mycur.execute("INSERT INTO client VALUES(?,?,?)", (nom, password, email))
                    message = "You are connected!\n"
                    broadcast1(message, nom)
                    th = threading.Thread(target=handle_client, args=(client,))
                    th.start()
            else:
                client.detach()
        else:
            threading.Thread(target=sende,args=(client,na)).start()
        conn .commit()
        conn.close()
reciver()