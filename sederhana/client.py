from PodSixNet.Connection import ConnectionListener, connection
import sys
from thread import *
from time import sleep


class Client(ConnectionListener):
    def __init__(self, host, port):
        self.Connect((host, port))
        t = start_new_thread(self.InputLoop, ())

    def Loop(self):
        connection.Pump()
        self.Pump()

    def InputLoop(self):
        while 1:
            connection.Send({"action": "pesan", "pesan": sys.stdin.readline().rstrip("\n")})

    def Network_connected(self, data):
        print "Berhasil konek ke server"

    def Network_hello(self, data):
        print "Pesan dari server: ", data['message']

    def Network_error(self, data):
        print 'error:', data['error'][1]
        connection.Close()

    def Network_disconnected(self, data):
        print 'Server disconnected'
        exit()


host, port = "localhost", 8000
c = Client(host, int(port))
while 1:
    c.Loop()
    sleep(0.001)
