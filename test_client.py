from http import client
import socket
import threading
import json
import cmd
import sys

class Client:
    # global variable keep track of list of users
    

    # constructor for the client
    def __init__(self,socket,id,nickname,hasJoined):

        #super().__init__()
        self.socket = socket
        self.id = id
        self.nickname = nickname
        self.hasJoined = hasJoined


    # function that handles post
    def post(self,message):
        self.socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.id,
            'username':self.nickname,
            'message': message
        }).encode())

    # function that handles joining
    def join(self, userName):
        self.nickname = userName
        client.hasJoined = True 

    # function that connects to a certain port
    def connect(self,address, portNum):
        self.socket.connect(address, portNum)


    

    


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = Client(clientSocket,None,None,False)
#print(client.isLogin)
client.socket.connect(('127.0.0.1', 8888))
userList = []
userID = 0

while True:
    print("Please type join [username] to join the chat or exit to quit the system")
    cmd = input()
    
    if cmd.startswith("join"):
        userName = cmd[5:]
        client.join(userName)
        userID = userID + 1
        client.userID = userID
        if client.nickname not in userList:
            userList.append(client.nickname)
        print(userList)
    elif cmd == exit:
        sys.exit("GoodBye!")
    else:
        print("Error: Command should be login [username] or exit for quit")

    while client.hasJoined is True:
        print("You are in! Any command?")
        cmd = input()

        if cmd.startswith("post"):
            message = cmd[5:]
            client.post(message)
            print(f"posted {message}")
        elif cmd == "users":
            print(userList)
        elif cmd.startswith("message"):
            MsgID = cmd[8:]
            print("TODO: Print the corresponding message in msg array")
        elif cmd == "leave":
            client.hasJoined = False
        elif cmd == "exit":
            sys.exit("GoodBye!")
        else:
            print("please enter connect to connect to a port, join to join a chatroom, post to post a message, users to see existing users, leave to leave the chatroom, message to retrieve a certain message, or exit to end the system.")
