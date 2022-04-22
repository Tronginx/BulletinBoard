from http import client
import socket
import threading
import json
import cmd
import sys

class Client:

    # constructor for the client
    def __init__(self,socket,id,nickname,isLogin):

        #super().__init__()
        self.socket = socket
        self.id = id
        self.nickname = nickname
        self.isLogin = isLogin


    # function that converts messages to json object for data transmission
    def send_message(self,message):
       
        self.socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.id,
            'username':self.nickname,
            'message': message
        }).encode())

    # function that handles login
    def login(self, userName):

        self.nickname = userName
        client.isLogin = True 

    # function that handles logout
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
    elif Client.isLogin is False:
        print("Error: Command should be login [username] or exit for quit")    

    if client.isLogin is True:
       print("You can send message now, or type in help to see all commands")
       cmd = input()
        # command for sending message
       if cmd.startswith("post"):
            message = cmd[5:]
            client.send_message(message)
            #client.isLogin = False
            print(f"posted {message}")
        # display user list
       elif cmd == "users":
            print(userList)
        # leave the chatroom
       elif cmd == "leave":
            client.isLogin = False
        # check a certain message
       elif cmd.startswith("message"):
            index = cmd[8:]
            #print(test_server.messageList[index])
       else:
            print("please enter connect to connect to a port, join to join a chatroom, post to post a message, users to see existing users, leave to leave the chatroom, message to retrieve a certain message, or exit to end the system.")
    else:
        print("You have to login to perform such action!")
    
       