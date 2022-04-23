import socket
import json
import pickle

messageList = ["user:1","sb:3","le:4","le:5"]
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(10)
while True:

    client_socket, address = server_socket.accept()
    msg = client_socket.recv(1024)
    obj = json.loads(msg)
    if obj['type'] == 'broadcast':
        msg = obj['username'] + ':' + obj['message']
        messageList.append(msg)
        print (msg)
        print(messageList)
    if obj['type'] == 'message':

        data = pickle.dumps(messageList)
        client_socket.send(data)
        
        
