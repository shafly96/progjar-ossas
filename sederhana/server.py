import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print data

    def Network_pesan(self, data):
        print "pesan: ", data['pesan']


class MyServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print 'koneksi baru: ', channel
        channel.Send({"action": "hello", "message": "hello client!"})


host, port = "localhost", 8000
myserver = MyServer(localaddr=(host, int(port)))
if myserver:
    print "Server nyala: ", host, ":", port
while True:
    myserver.Pump()
    sleep(0.001)
