import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print data

    def Network_pesan(self, data):
        print "pesan: ", data['pesan']

    def Network_pilih(self, data):
        self.gameid = data["gameid"]
        flag = data['flag']
        print "pilihan dari ", data['player'], "adalah ", data['flag']
        self._server.pilih(self.gameid, flag, data['player'])

    def Close(self):
        self._server.close(self.gameid)


class MyServer(PodSixNet.Server.Server):
    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.currentIndex = 0
        self.games = []
        self.queue = None

    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print 'koneksi baru: '
        print 'channel = ', channel
        print 'addr = ', addr
        # channel.Send({"action": "hello", "message": "hello client!"})
        if self.queue == None:
            self.currentIndex += 1
            channel.gameid = self.currentIndex
            self.queue = Game(channel, self.currentIndex)
        else:
            channel.gameid = self.currentIndex
            self.queue.player1 = channel

            self.queue.player0.Send(
                {"action": "startgame", "player": 0, "gameid": self.queue.gameid}
            )
            self.queue.player1.Send(
                {"action": "startgame", "player": 1, "gameid": self.queue.gameid}
            )
            self.games.append(self.queue)
            self.queue = None

    def pilih(self, gameid, flag, player):
        game = [a for a in self.games if a.gameid == gameid]
        if len(game) == 1:
            game[0].pilih(gameid, flag, player)

    def close(self, gameid):
        try:
            game = [a for a in self.games if a.gameid == gameid][0]
            game.player0.Send({"action": "close"})
            game.player1.Send({"action": "close"})
        except:
            pass


class Game:
    def __init__(self, player0, currentIndex):
        self.player0 = player0
        self.player1 = None
        self.gameid = currentIndex

    def pilih(self, gameid, flag, player):
        if player == 1:
            print 'flag(',flag,') dikirim ke player 0'
            self.player0.Send({"action": "pilih", "flag": flag, "gameid": gameid})
        else:
            print 'flag(', flag, ') dikirim ke player 1'
            self.player1.Send({"action": "pilih", "flag": flag, "gameid": gameid})


host, port = "10.151.62.99", 8000
myserver = MyServer(localaddr=(host, int(port)))
if myserver:
    print "Server nyala: ", host, ":", port
while True:
    myserver.Pump()
    sleep(0.001)
