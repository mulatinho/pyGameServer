import GameServer
import time

class CoreServer:
    def __init__(self):
        '''initial server setup'''
        print "hey, I'm the CoreServer and I exist"
        self.loopServer()
    
    def loopServer(self):
        print "method loopServer() here to serve"
        GameServer.GameServer()
