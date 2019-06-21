# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See LICENSE for more details.
#
# Author: Alexandre Mulatinho <alex@mulatinho.net>

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
