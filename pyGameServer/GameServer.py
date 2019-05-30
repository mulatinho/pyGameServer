import socket
import select
import time
from sys import platform
    
class GameServer:
    socketServer = None
    user_max = 200
    connections = {}; requests = {}; address = {}; 
    pollFunc = {}; pollEvents = {};
    pollIn = {}; pollOut = {}; pollHUP = {};
    
    def __init__(self):
        '''GameServer is the the TCP/IP server of the pyGameServer'''
        print "GameServer() init"
        self.socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socketServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socketServer.bind(("127.0.0.1", 2020))
        self.socketServer.listen(self.user_max)
    
        self.setPollFunction()
            
        try:
            while True:
                events = self.pollFunc.poll(1)
                for fileno, event in events:
                    if fileno == self.socketServer.fileno():
                        clientConnection, address = self.socketServer.accept()
                        clientConnection.setblocking(0)
                        
                        print "connection estabilished from " + str(address)
                        
                        self.pollFunc.register(clientConnection.fileno(), self.pollEvents)
                        self.connections[clientConnection.fileno()] = clientConnection
                        self.address[clientConnection.fileno()] = str(address)
                        self.requests[clientConnection.fileno()] = b''
                        
                    elif event & self.pollIn:
                        clientData = b'OK'
                        while True:
                            clientData = self.connections[fileno].recv(1024)
                            
                            if len(clientData) != 0:
                                self.requests[fileno] += self.connections[fileno].recv(1024)
                            else:
                                self.connections[fileno].send(b'"hey man!!"')
                                self.requests[fileno] = b''
                                self.pollFunc.modify(fileno, self.pollOut)
                                break
                        
                    elif event & self.pollOut:
                        self.pollFunc.modify(fileno, self.pollHUP)
                        
                    elif event & self.pollHUP:
                        print "connection closed from " + str(fileno)
                        'connection closed from {} at address {}'.format(2,3)
                        'connection closed from {} at address {}'.format(str(fileno), self.address[fileno])
                        self.pollFunc.unregister(fileno)
                        self.connections[fileno].close()
                        del self.connections[fileno]
                        del self.address[fileno]
                
                print "and the loops goes on, with this connections: " + str(len(self.connections))           
                time.sleep(0.750)
        finally:
            print "Thats it!"
        
    def setPollFunction(self):
        if platform == "linux" or platform == "linux2":
            self.pollFunc = select.epoll()
            self.pollIn = select.EPOLLIN
            self.pollOut = select.EPOLLET
            self.pollHUP = select.EPOLLHUP
            self.pollEvents = select.EPOLLIN | select.EPOLLET
            self.pollFunc.register(self.socketServer.fileno(), self.pollEvents)
        else:
            self.pollFunc = select.poll()
            self.pollIn = select.POLLIN
            self.pollOut = select.POLLOUT
            self.pollHUP = select.POLLHUP
            self.pollEvents = select.POLLIN | select.POLLOUT
            self.pollFunc.register(self.socketServer.fileno(), select.POLLIN | select.POLLOUT)
