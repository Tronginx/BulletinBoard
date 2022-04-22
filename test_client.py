from http import client
import socket
import threading
import json
import cmd

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
            'message': message
        }).encode())


    def login(self, userName):

        nickname = userName

        self.socket.send(json.dumps({
            'type': 'login',
            'nickname': nickname
        }).encode())



clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = Client(clientSocket,None,None,False)
#print(client.isLogin)
client.socket.connect(('127.0.0.1', 8888))

while True:
    print("Please type your command:")
    cmd = input()
    
    if cmd.startswith("login"):
        userName = cmd[6:]
        client.login(userName)
        break

    if cmd.startswith("send"):
        message = cmd[5:]
        client.send_message(message)
        print(f"sent {message}")
        break
        