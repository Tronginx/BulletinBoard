from re import S
import socket
import json
import pickle


messageList = ["user1:a","user2:b"]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(10)
server_socket, address = server_socket.accept()

data = pickle.dumps(messageList)
server_socket.send(data)
server_socket.close()
