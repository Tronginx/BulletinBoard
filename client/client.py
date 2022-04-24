import socket
import threading
import json
from cmd import Cmd


class Client(Cmd):
    prompt = ''
    intro = 'Welcome to the BulletinBoard!\n' + 'Please type in command or help to see all the commands!'

    # constructor for the client object
    def __init__(self):
        super().__init__()
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__id = None
        self.__userName = None
        self.__hasJoined = False

    def __receive_message_thread(self):
        while self.__hasJoined:
            try:
                buffer = self.__socket.recv(1024).decode()
                obj = json.loads(buffer)
                print('[' + str(obj['sender_nickname']) + '(' + str(obj['sender_id']) + ')' + ']', obj['message'])
            except Exception:
                print("Error! Cannot retrieve data from the server")

    def __send_message_thread(self, message):
        self.__socket.send(json.dumps({
            'type': 'broadcast',
            'sender_id': self.__id,
            'message': message
        }).encode())

    def start(self):
        print("Please enter the same address again for connection!")
        address = input()
        print("Please enter the port number again for connection!")
        port = input()
        self.__socket.connect((address, int(port)))
        self.cmdloop()

    def do_login(self, args):
        nickname = args.split(' ')[0]

        # send username to the server and retrieve 
        self.__socket.send(json.dumps({
            'type': 'login',
            'nickname': nickname
        }).encode())
        
        # read the data from the server
        try:
            buffer = self.__socket.recv(1024).decode()
            obj = json.loads(buffer)
            if obj['id']:
                self.__userName = nickname
                self.__id = obj['id']
                self.__hasJoined = True
                print("Congratulations! You are in!")

                # 开启子线程用于接受数据
                thread = threading.Thread(target=self.__receive_message_thread)
                thread.setDaemon(True)
                thread.start()
            else:
                print("Error! Failed to join the chat")
        except Exception:
            print("Error! Cannot retrieve data from the server!")

    def do_send(self, args):
        """
        发送消息
        :param args: 参数
        """
        message = args
        # 显示自己发送的消息
        print('[' + str(self.__userName) + '(' + str(self.__id) + ')' + ']', message)
        # 开启子线程用于发送数据
        thread = threading.Thread(target=self.__send_message_thread, args=(message,))
        thread.setDaemon(True)
        thread.start()

    def do_logout(self, args=None):
        """
        登出
        :param args: 参数
        """
        self.__socket.send(json.dumps({
            'type': 'logout',
            'sender_id': self.__id
        }).encode())
        self.__hasJoined = False
        return True

    def do_help(self, arg):
        print('You can type in join [username] to join the bulletinboard using the username!')
        print('You can use post [message] to post the message that you want to send to the chat!')
        print('You can type in leave to leave the chat!')
