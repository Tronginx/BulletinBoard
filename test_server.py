import socket
import json
import pickle
import sys

messageList = []
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8888))
server_socket.listen(10)

while True:
    client_socket, address = server_socket.accept()
    try:
        while True:
            msg = client_socket.recv(1024)
            obj = json.loads(msg)
            if obj['type'] == 'broadcast':
                msg = obj['username'] + ':' + obj['message']
                messageList.append(msg)
                print (msg)
                print(messageList)
            elif obj['type'] == 'message':
                data = pickle.dumps(messageList)
                client_socket.send(data)
    except:
        sys.exit("Failed to establish connection")
    finally:
        client_socket.close()
        
        
