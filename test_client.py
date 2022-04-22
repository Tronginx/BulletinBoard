from http import client
import socket
import threading
import json
import cmd
import sys

class Client:

    def __init__(self,socket,id,nickname,isLogin):

        #super().__init__()
        self.socket = socket
        self.id = id
        self.nickname = nickname
        self.isLogin = isLogin



    def send_message(self,message):
       
        self.socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.id,
            'username':self.nickname,
            'message': message
        }).encode())


    def login(self, userName):

        self.nickname = userName
        client.isLogin = True 

    def logout(self):
        client.isLogin = False 
    


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = Client(clientSocket,None,None,False)
#print(client.isLogin)
client.socket.connect(('127.0.0.1', 8888))
userList = []

id = 0
while True:
    print("Please type login [username] to send message:")
    cmd = input()
    
    if cmd.startswith("exit"):
        sys.exit("Goodbye!")

    if cmd.startswith("login"):
        userName = cmd[6:]
        client.login(userName)
        client.id = id +1
        userList.append(client.nickname)
        print(userList)
    else:
        print("Error: Command should be login [username]")    

    if client.isLogin is True:
       print("You can send message now")
       cmd = input()
       if cmd.startswith("send"):
            message = cmd[5:]
            client.send_message(message)
            client.isLogin = False
            print(f"sent {message}")
    else:
        print("You have to login before sending message!")
    
       