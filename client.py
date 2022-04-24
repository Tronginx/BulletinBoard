import socket
import json
import sys
import pickle

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

    # function that handles message
    def message(self):
        self.socket.send(json.dumps({
            'type': 'message'
        }).encode())

    # function that handles joining
    def join(self, userName):
        self.nickname = userName
        client.hasJoined = True 


try:

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client = Client(clientSocket,None,None,False)
    print("Please type host address you want to connect:")
    host = input()
    print("Please type port number you want to connect:")
    port = input()
    client.socket.connect(('127.0.0.1', 8888))
    userList = []
    userID = 0

    while True:
        print("Please type join [username] to join the chat or exit to quit the system")
        cmd = input()
        
        if cmd.startswith("join"):
            userName = cmd[5:].strip()
            client.join(userName)
            userID = userID + 1
            client.userID = userID
            if client.nickname not in userList:
                userList.append(client.nickname)
                print(userList)
            else:
                sys.exit("User name is existed. Try another one")
        elif cmd == "exit":
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
                print("The users are: ")
                for user in userList:
                    print(user)
                    
                
            elif cmd.startswith("message"):
                sender = cmd[8:]
                sender_len = len(sender)
                client.message()
                data = client.socket.recv(4096)
                data_arr = pickle.loads(data)
                for msg in data_arr:
                    if msg[:sender_len]==sender:
                        print(msg)
            elif cmd == "leave":
                client.hasJoined = False
            elif cmd == "exit":
                sys.exit("GoodBye!")
            else:
                print("[help] Keyword post [message] for posting message")
                print("[help] Keyword message [username] to see the message sent of a certain user")
                print("[help] Keyword users to see current user list")
                print("[help] Keyword leave to leave the groupchat")
                print("[help] Keyword exit for forcequit the system")

except:
   sys.exit("ERROR: Connection cannot established")