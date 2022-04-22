from http import client
import socket
import pickle

class Client:

    def __init__(self,socket,id,nickname,isLogin):

        #super().__init__()
        self.socket = socket
        self.id = id
        self.nickname = nickname
        self.isLogin = isLogin


clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = Client(clientSocket,None,None,False)
#print(client.isLogin)
client.socket.connect(('127.0.0.1', 8888))
data = client.socket.recv(4096)
data_arr = pickle.loads(data)
print(data_arr)