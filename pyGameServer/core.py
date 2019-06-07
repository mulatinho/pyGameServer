import GameServer as GS

class Config:
    pass

class CoreServer(object):
    config = Config()

    def __init__(self):
        """initial server setup"""
        print "hey, I'm the CoreServer and I exist"
        self.start()

    def start(self):
        print "method loopServer() here to serve"
        instance = GS.GameServer()
        instance.serverLoop()
