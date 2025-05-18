# Instant Messaging Application  

A simple real-time messaging application built with Python, Tkinter for the GUI, and SQLite for database management. It supports private messaging, group chats, user authentication, and more.  

---

## Features  

- **User Authentication**: Sign up and log in with a username, password, and email.  
- **Private Messaging**: Send direct messages to other users.  
- **Group Chats**: Create groups and add multiple participants.  
- **Message History**: View chat history for groups and private conversations.  
- **Profile Management**: Change your username or recover forgotten passwords.  
- **Real-Time Communication**: Uses sockets for instant message delivery.  

---

## Prerequisites  

### Core Dependencies  
- **Python 3.7+** ([Download Python](https://www.python.org/downloads/))  

### Libraries by Category  
| Category                     | Libraries/Packages             | Installation Command (if needed)          |  
|------------------------------|---------------------------------|-------------------------------------------|  
| **Graphical Interface**      | Tkinter, CustomTkinter*        | `pip install customtkinter`               |  
| **Database Management**      | SQLite3 (built-in)             | *No installation required*                |  
| **Network Communication**    | Socket (built-in)              | *No installation required*                |  
| **Concurrency**              | Threading (built-in)           | *No installation required*                |  
| **Image Handling**           | Pillow                         | `pip install pillow`                      |  

*Note: Tkinter is included in Python's standard library. CustomTkinter is optional for enhanced UI.*  

---

## Installation  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/aalaliayoub/instaChat.git  
   cd instaChat
2. Run the server:
   ```bash
   python server10.py
3. Launch the client:
   ```bash
   python client10.py  
