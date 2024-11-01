import socket
import time
import tkinter
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as tb
from tkinter import scrolledtext
from tkinter import messagebox
from threading import Thread
import ttkbootstrap
import json
import os
import sys
import webbrowser
from PIL import ImageTk
formatt="utf-8"
global r1,fenetre,r2,r3,r4,e1,entr1,Mymenu,row,e3,tt,w3,Mymenu2,entry,entry1,w1,test,row2,passwordconfigure,le1,b22,menu,b343,th,texth2,texth,text1, window,root,nomes,i,name,le,j,listgroupe,opti0n,b34,b2,le3,password1,l1,listgroupe2
client_iip = socket.gethostbyname(socket.gethostname())
clientppport = 12345
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((client_iip, clientppport))
noms=[]
def enter10(e):
    global r1
    r1.delete(0,"end")
def sorti10(e):
    global r1
    name=r1.get()
    if name=="":
        r1.insert(0,"nom d'utilisateur")

def enter40(e):
    r4.delete(0,"end")
def sorti40(e):
    name=r4.get()
    if name=="":
        r4.insert(0,"confirmer le mot de passe")
def enter20(e):
    r2.delete(0,"end")
def sorti20(e):
    email=r2.get()
    if email=="":
        r2.insert(0,"Email Ex:simo2007@gmail.com")
def enter30(e):
    r3.delete(0,"end")
def sorti30(e):
    code=r3.get()
    if code=="":
        r3.insert(0,"Mot de passe")

def sendinformation():
    global row,listgroupe,name,fenetre,passwordconfigure,client,window,test
    name=r1.get()
    listgroupe.append(name)
    email=r2.get()
    password=r3.get()
    passwordconfigure=r4.get()
    messapasswordge=f"{name}/{password}/{email}/{passwordconfigure}"
    client.send(messapasswordge.encode(formatt))
    information=client.recv(1024).decode(formatt)
    noms=information.split(sep="/")
    row=noms
    if name in noms:
        resultat = messagebox.askretrycancel("ERREUR", "vous avez deja un compte clique sur signin si non entrez un autre username ")
        if resultat:
            client.detach()
            client_iip = socket.gethostbyname(socket.gethostname())
            clientppport = 12345
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((client_iip, clientppport))
        else:
            client.detach()
            window.destroy()
    elif passwordconfigure!=password:
        messagebox.showwarning("Message Erreur", "confirmation du mot de passe est incorrect!")
        client.detach()
        client_iip = socket.gethostbyname(socket.gethostname())
        clientppport = 12345
        client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((client_iip, clientppport))
    else:
        window.withdraw()
        fenetreprincipal(r1,client)
def signup():
    global r1, r2, r3,fenetre, r4,window,passwordconfigure
    fenetre.destroy ()
    window =tk.Tk()
    window.geometry("770x480")
    window.config (bg="white")
    window.title("instant Messagiing")
    icone_path = resource_path("messager.ico")
    Image.open(resource_path("messager.ico")).save(icone_path)
    window.iconbitmap(icone_path)
    window.resizable(False, False)
    image=ImageTk.PhotoImage (Image.open(resource_path("image2.jpg")))
    qq=tkinter.Label (window ,image=image)
    qq.place(x=0,y=0)
    l2 = tk.Label(window, text="Authentification", font=("Microsoft Yahei UI Light", 20, 'bold'), bg="white", fg="blue")
    l2.place(x=435,y=80)
    r1 = tk.Entry(window, border=0, font=("Microsoft Yahei UI Light", 11), width=26,bg="white")
    r1.place(x=434,y=140)
    r1.insert(0, "User name")
    r1.bind("<FocusIn>", enter10)
    r1.bind("<FocusOut>", sorti10)
    fr1 = tk.Frame(window, width=230, height=3, bg="black").place(x=434,y=160)
    r2 = tk.Entry(window, border=0, font=("Microsoft Yahei UI Light", 11), width=26)
    r2.place(x=434,y=200)
    r2.insert(0, "Email ")
    r2.bind("<FocusIn>", enter20)
    r2.bind("<FocusOut>", sorti20)
    fr2 = tk.Frame(window, width=230, height=3, bg="black")
    fr2.place(x=434,y=220)
    r3 = tk.Entry(window, border=0, font=("Microsoft Yahei UI Light", 11), width=26)
    r3.place(x=434,y=280)
    r3.insert(0, "Password")
    r3.bind("<FocusIn>", enter30)
    r3.bind("<FocusOut>", sorti30)
    fr3 = tk.Frame(window, width=230, height=3, bg="black").place(x=434,y=300)
    r4 = tk.Entry(window, border=0, font=("Microsoft Yahei UI Light", 11), width=26)
    r4.place(x=434,y=340)
    r4.insert(0, "Password confirmation")
    r4.bind("<FocusIn>", enter40)
    r4.bind("<FocusOut>", sorti40)
    fr4 = tk.Frame(window, width=230, height=3, bg="black").place(x=434,y=360)
    b1 = tk.Button(window, width=33, bg="#57a1f8", pady=7, text="Enregistrer", fg="white", border=0,cursor='hand2',command=lambda:Thread(target=sendinformation).start()).place(x=435,y=365)
    b23=tk.Button(window,text="SignIn",width=33,fg="white",bg="#57a1f8",pady=7,border=0,cursor='hand1',command=lambda:[window.destroy(),signin()]).place(x=434,y=400)
    window.mainloop()

def sendh(client):
    global texth2,texth,i,name,tt,mumenu,nameselectioner,e3,names,row,row2,le3,name
    while True:
        text1=client.recv(1024).decode(formatt)
        lis = text1.split(sep="/")
        message = lis[0]
        if len(lis)==1:
            texth.configure(state=tk.NORMAL)
            texth.insert(END,f"{message}")
            texth.yview(END)
            texth.configure(state=tk.DISABLED)
        elif len(lis)==5 :
            if lis[1]==name:
                groupadmin(client)
            else:
                groupall(client)
        elif len(lis)==2:
            texth2.configure(state=tk.NORMAL)
            texth2.insert(END, f"{message}\n")
            texth2.yview(END)
            texth2.configure(state=tk.DISABLED)
        elif len(lis)==3:
            lesnom=json.loads(lis[0])
            liste=[]
            for nom in lesnom :
                liste.append(nom[0])
            if name in liste:
                liste.remove(name)
            if len(liste)==0:
                liste.append(" ")
            row=liste
            le3=tk.OptionMenu(tt, option, *row)
            le3.place(x=300, y=490)
            row2=liste
        elif len(lis)==4:
            lesmessage=json.loads(message)
            texth2.configure(state=tk.NORMAL)
            for messa in lesmessage:
                texth2.insert(END, f"{messa[0]}\n")
                texth2.yview(END)
            texth2.configure(state=tk.DISABLED)

def enter1(e):
    global w1
    w1.delete(0,"end")
def sorti1(e):
    name=w1.get()
    if name=="":
        w1.insert(0,"Username")
def enter3(e):
    w3.delete(0,"end")
def sorti3(e):
    code=w3.get()
    if code=="":
        w3.insert(0,"Password")
def Envoyer_message(message,client):
    if message=="Historique":
        client.send("Historique".encode(formatt))
    else :
        client.send(message.encode(formatt))
def afichier_historique(client):
    global texth2
    textt = client.recv(1024).decode(formatt)
    print(textt)
    texth2.insert(END, textt)
def sortt(entry,client):
    text2= entry.get()
    if text2!=" ":
        client.send(text2.encode(formatt))
    entry.delete(0, "end")
def sort(mess):
    global e3,option,listgroupe,b2,b34,le,entr1,name,l1,th,listgroupe2,le1,b22,b343,Mymenu2,menu
    if mess =="creegroupe":
        b2.destroy()
        le.destroy()
        b34.destroy()
        listgroupes =json.dumps(listgroupe)
        listfinal=f"{listgroupes}@addgroup"
        client.send(listfinal.encode(formatt))
    elif mess=="addnewnabers":
        le1.destroy()
        b22.destroy()
        b343.destroy()
        listgroupese = json.dumps(listgroupe2)
        listfinal = f"{listgroupese}@addgroup@new"
        client.send(listfinal.encode(formatt))
        listgroupe2=[]
    elif mess=="modifierlenom":
        nom=entr1.get()
        name=nom
        nnom=f"{nom}!changerlenom"
        menu.delete("Profil")
        Mymenu3=Menu(menu)
        menu.add_cascade(label="Profil",menu=Mymenu3)
        Mymenu3.add_command(label=f"nom:{nom}")
        client.send(nnom.encode(formatt))
        listgroupe.append(nom)
        th.withdraw()
    else :
        text3 = e3.get()
        name1= option.get()
        if text3!=" " and name1!=" ":
            text3 = f"{text3}/{name1}"
            client.send(text3.encode(formatt))
        e3.delete(0, "end")
def modifier():
    global entr1,th
    th=tk.Tk ()
    th.title("Parametre")
    icone_path = resource_path("messager.ico")
    Image.open(resource_path("messager.ico")).save(icone_path)
    th.iconbitmap(icone_path)
    entr1=tk.Entry(th,width=25)
    entr1.pack()
    dd1=tk.Button(th,text="modefier",bg="pink",command=lambda:sort("modifierlenom"))
    dd1.pack()
    th.mainloop()
def clearchat():
    global texth2
    texth2.configure(state=tk.NORMAL)
    texth2.delete('1.0',"end")
    texth2.configure(state=tk.DISABLED)
def groupadmin(client):
    global texth2,tt,listgroupe,Mymenu,entry
    texth2 = tk.scrolledtext.ScrolledText(tt, border=4, width=65, height=25)
    texth2.place(x=600, y=30)
    entry = tk.Entry(tt, width=40)
    entry.place(x=770, y=460)
    Thread(target=sendh, args=(client,)).start()
    b=tk.Button(tt, text="Envoyer", command=lambda: Thread(target=sortt, args=(entry, client)).start())
    b.place(x=850, y=490)
    entry.bind("<Return>",sendd2)
    b4 = tk.Button(tt, text="Historique", bg="cyan",command=lambda: Envoyer_message("Historique", client))
    b4.place(x=845, y=525)
    Mymenu.add_command(label="add participants",command=lambda:groupe1(client))
    Mymenu.add_command (label="Clear chat group",command=clearchat)
def sendd3(event):
    global entry1
    message=entry1.get()
    client.send(message.encode(formatt))
    entry1.delete(0,'end')
def groupall(client):
    global texth2,tt,listgroupe,Mymenu,entry1
    texth2 = tk.scrolledtext.ScrolledText(tt, border=4, width=65, height=25)
    texth2.place(x=600, y=30)
    entry1 = tk.Entry(tt, width=40)
    entry1.place(x=770, y=460)
    Thread(target=sendh, args=(client,)).start()
    b = tk.Button(tt, text="Envoyer", command=lambda: Thread(target=sortt, args=(entry1, client)).start())
    b.place(x=850, y=490)
    entry1.bind("<Return>",sendd3)
    b4 = tk.Button(tt, text="Historique", bg="cyan", command=lambda: Envoyer_message("Historique", client))
    b4.place(x=845, y=525)
    Mymenu.add_command(label="Clear chat group", command=clearchat)
def actualiser():
    global le3,row
    le3.destroy()
    if " " in row and len(row)>1:
        row.remove(" ")
    client.send("list/new/list".encode(formatt))

def clear():
    global texth
    texth.configure(state=tk.NORMAL)
    texth.delete('1.0','end')
    texth.configure(state=tk.DISABLED)
def exitt():
    global name,row,le,tt,fenetre
    res=messagebox.askyesno("Messanger","Souhaitez-vous vraiment vous deconnecter")
    if res:
        client.detach()
        tt.destroy()
def addtolist(option):
    global listgroupe,b34,name,noms
    if len(listgroupe)>1:
        b34.destroy()
    nom=option.get()
    if nom !=" ":
        listgroupe.append(nom)
        noms.append(nom)
    b34=tk.Button(tt,text="creer",width=5,command=lambda:sort("creegroupe"))
    b34.place(x=300,y=0)

def addtolist2(option):
    global listgroupe2,b343,name
    if len(listgroupe2)>=1:
        b343.destroy()
    nom=option.get()
    if nom!=" ":
        listgroupe2.append(nom)
        noms.append(nom)
    b343=tk.Button(tt,text="add to groupe",width=10,command=lambda:sort("addnewnabers"))
    b343.place(x=300,y=0)
def opensite():
    webbrowser.open("https://tkinter.com/")

def groupe(client):
    global tt,row,le,b2,listgroupe,name
    if name not in listgroupe :
        listgroupe.append(name)
    option = tk.StringVar(tt)
    le = tk.OptionMenu(tt, option, *row)
    le.place(x=60, y=3)
    b2 = tk.Button(tt, text="add",command=lambda:addtolist(option))
    b2.place(x=190, y=0)
def sendd2(event):
    global entry
    message=entry.get()
    client.send(message.encode(formatt))
    entry.delete(0,'end')
def sendd(event):
    global e3,option
    nsm = option.get()
    if nsm!=" ":
        nes = e3.get()
        message = f"{nes}/{nsm}"
        client.send(message.encode(formatt))
    e3.delete(0,'end')
def groupe1(client):
    global tt,row,le1,b22,listgroupe2,noms
    option = tk.StringVar(tt)
    for nom in noms:
        if nom in row:
            row.remove(nom)
    if len(row)!=0:
        le1 = tk.OptionMenu(tt, option, *row)
        le1.place(x=60, y=3)
        b22 = tk.Button(tt, text="add", command=lambda: addtolist2(option))
        b22.place(x=190, y=0)
    else:
        messagebox.showinfo("Messanger","la liste des ami est vide")
def fenetreprincipal(w1,client):
    global texth, tt,fenetre, window,w3,e3,e1,texth2,name,names,row,le3,option,menu,Mymenu,l1,Mymenu2
    name=w1.get()
    tt = tk.Tk()
    tt.config(bg="cyan")
    tt.title("chatting")
    tt.geometry("1180x600")
    tt.resizable(False, False)
    icone_path = resource_path("messager.ico")
    Image.open(resource_path("messager.ico")).save(icone_path)
    tt.iconbitmap(icone_path)
    texth = tk.scrolledtext.ScrolledText(tt, border=4, width=65, height=25)
    texth.place(x=20, y=30)
    e3 = tk.Entry(tt, width=40,fg="black")
    e3.place(x=150, y=460)
    Thread(target=sendh,args=(client,)).start()
    b2 = tkinter.Button(tt,text="Envoyer",font=10,command=lambda:Thread(target=sort,args=("",)).start())
    b2.place(x=220, y=490)
    e3.bind("<Return>",sendd)
    option = tk.StringVar(tt)
    le3=tk.OptionMenu(tt,option,*row)
    le3.place(x=300,y=490)
    menu=Menu (tt)
    tt.config (menu=menu)
    Mymenu= Menu(menu,cursor="hand2")
    Mymenu1=Menu(menu)
    Mymenu2=Menu(menu)
    menu.add_cascade(label="Options",font="bold 60", menu=Mymenu,)
    menu.add_cascade(label="Profil",menu=Mymenu2)
    menu.add_cascade(label="Parametre", menu=Mymenu1)
    menu.add_cascade(label="Help",command=opensite)
    Mymenu.add_command(label="Clear chat", command=clear)
    Mymenu.add_command(label="Exit", command=exitt)
    Mymenu.add_command(label="New groupe", command=lambda: groupe(client))
    Mymenu.add_command(label="Actualiser", command=lambda:actualiser())
    Mymenu1.add_command(label="Changer votre nom",command=lambda:modifier())
    Mymenu2.add_command(label=f"nom: {name}")
    tt.mainloop()
def afiiche():
    global fenetre,password1
    messagebox.showinfo("instant Messaging",f"<#> {password1} est votre mot de passe.Ne le partage pas" )

def sendname():
    global w3,name,row,password1,w1,client
    name = w1.get()
    password = w3.get()
    paassname=f"{name}/{password}"
    client.send(paassname.encode(formatt))
    toot = client.recv(1024).decode(formatt)
    row =toot.split(sep='/')
    if name in row :
        row.remove(name)
    if name not in toot:
        resultat1 = messagebox.askretrycancel("ERREUR", "Voua n'avez pas de compte cliquer sur SignUp")
        if resultat1:
            client.detach()
            client_iip = socket.gethostbyname(socket.gethostname())
            clientppport = 12345
            client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect((client_iip, clientppport))
        else:
            client.detach()
            fenetre.destroy()
    elif name in toot:
        password1 = client.recv(1024).decode(formatt)
        if password != password1:
            resultat = messagebox.askretrycancel("ERREUR", "Motde passe inccorect")
            if resultat:
                client.detach()
                client_iip = socket.gethostbyname(socket.gethostname())
                clientppport = 12345
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((client_iip, clientppport))
            else:
                fenetre.destroy()
                client.detach()
        else:
            listgroupe.append(name)
            fenetre.withdraw()
            fenetreprincipal(w1,client)
def resource_path(relative_path):
    try :
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path,relative_path)

def signin():
    global w1,w3,fenetre,client,listgroupe,test,window,row2,listgroupe2
    listgroupe2 =[]
    row2 =[]
    noms=[]
    listgroupe=[]
    fenetre = tk.Tk()
    fenetre.geometry("650x430")
    fenetre.title("Messanger")
    fenetre.resizable(False, False)
    fenetre.config(bg="white")
    icone_path = resource_path("messager.ico")
    Image.open(resource_path("messager.ico")).save(icone_path)
    fenetre.iconbitmap(icone_path)
    logo = ImageTk.PhotoImage(Image.open(resource_path("image1.jpg")))
    l1 = tk.Label(fenetre, image=logo, border=0,width=690,bg="white")
    l1.image = logo
    l1.place(x=0,y=-10)
    l2 = tk.Label(fenetre, text="Sign in",bg="white", font=("Microsoft Yahei UI Light", 25, 'bold'),fg="blue")
    l2.place(x=440, y=20)
    w1 = tk.Entry(fenetre, border=0,bg="white" , font=("Microsoft Yahei UI Light", 11), width=26)
    w1.place(x=400, y=110)
    w1.insert(0, "User name")
    w1.bind("<FocusIn>", enter1)
    w1.bind("<FocusOut>", sorti1)
    fr2 = tk.Frame(fenetre, width=200, height=2, bg="black").place(x=400, y=130)
    w3 = tk.Entry(fenetre, border=0, font=("Microsoft Yahei UI Light", 11), width=26)
    w3.place(x=400, y=180)
    w3.insert(0, "Password")
    w3.bind("<FocusIn>", enter3)
    w3.bind("<FocusOut>", sorti3)
    fr2 = tk.Frame(fenetre, width=200, height=2, bg="black").place(x=400, y=200)
    b1 = tk.Button(fenetre, width=29, bg="#57a1f8", pady=7, text="se conneter", cursor="hand2",fg="white", border=0,command=lambda:Thread(target=sendname).start()).place(x=400, y=220)
    l5 = tk.Label(fenetre, text="Si vous n'avez pas de compte cliquez sur Sign up",border=0, bg="white", font=("Arial",11)).place(x=300,y=260)
    b2 = tk.Button(fenetre, text="Sign up", fg="white", bg="#57a1f8", width=29, height=2, border=0, cursor="hand2",command=lambda:signup()).place(x=400, y=300)
    b1212=tk.Button(fenetre,text="Recuperer le mot de passe ",width=29,command=afiiche,cursor="hand2",bg="#57a1f8",border=0,height=2,fg="white")
    b1212.place(x=400,y=360)
    fenetre.mainloop()
signin()