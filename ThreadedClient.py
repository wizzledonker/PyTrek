import socket
import threading

class PyTrekClient(object):
    def __init__(self, hostname):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = hostname
        self.port = 23545
        self.isClose = False
        
    def start(self):
        self.sock.connect((self.host,self.port))
        threading.Thread(target = self.listen).start()
        print("Client Started...")
        
    def listen(self):
        # Listen for requests
        while not self.isClose:
          data = self.sock.recv(2048)
          if data and hasattr(self, 'messageRecieved'):
            self.messageRecieved(data)
          
    def setMessageRecievedCallback(self, callback):
        self.messageRecieved = callback
            
    def close(self):
        self.isClose = True
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((self.host, self.port))
        self.sock.close()
        
    def sendMessage(self, msg):
        self.sock.send(msg)
    
    

