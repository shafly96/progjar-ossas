from PodSixNet.Connection import ConnectionListener, connection
from thread import *
import pygame
from time import sleep, time


class Elemental(ConnectionListener):
    def __init__(self, host, port):
        self.gameid = None
        self.running = False
        self.Connect((host, port))
        self.belumMilih = True
        print 'masuk init'
        t = start_new_thread(self.Load1, ())
        print 'thread started'

    def Network_startgame(self, data):
        self.playerid = data["player"]
        self.running = True
        self.gameid = data["gameid"]
        connection.Send({'action': 'pesan', 'pesan': 'startgame'})

    def Network_connected(self, data):
        print "Berhasil terhubung ke server"

    def Network_pilih(self, data):
        self.belumMilih = False
        if self.gameid == data['gameid']:
            self.flag2 = data['flag']

    def Network_error(self, data):
        print 'error:', data['error']
        connection.Close()

    def Network_close(self, data):
        exit()

    def Network_disconnected(self, data):
        print 'Server disconnected'
        exit()

    def Loop(self):
        connection.Pump()
        self.Pump()

    def Load1(self):
        # membuat kotak
        pygame.init()
        self.screen = pygame.display.set_mode((690, 400))
        pygame.display.set_caption("Elemental Fight")
        self.clock = pygame.time.Clock()

        # inisialisasi
        # self.running = True

        # inisialisasi posisi client ketika klik element
        self.xpos = -1
        self.ypos = -1

        # membuat 60 fps
        self.clock.tick(60)

        # self.tunggu()

        # warna bg
        self.screen.fill((255, 255, 255))

        # inisialisasi objek
        self.initGraph()

        # membuat tampilan permainan
        if not self.running:
            # thread = Thread(target=self.drawBoard())
            # thread.start()
            self.drawBoard()

        # untuk mengecek sudahkah ada musuh yang masuk
        while not self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            sleep(0.01)
        # print 'mau load 2 neh'
        self.Load2()

    def Load2(self):
        self.drawBoard2()
        # running program
        self.flag1 = None
        self.flag2 = None
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                # elif event.type == pygame.MOUSEBUTTONDOWN:
                # 	print "koordinat = (%d, %d)"%event.pos
                elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] < 228 and event.pos[1] < 275 and \
                                event.pos[
                                    1] > 50:
                    print "daun"
                    self.flag1 = 1
                    connection.Send(
                        {"action": "pilih", "gameid": self.gameid, "flag": self.flag1, "player": self.playerid}
                    )
                elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 227 and event.pos[0] < 463 and \
                                event.pos[
                                    1] < 275 and event.pos[1] > 50:
                    print "api"
                    self.flag1 = 2
                    connection.Send(
                        {"action": "pilih", "gameid": self.gameid, "flag": self.flag1, "player": self.playerid}
                    )
                elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 462 and event.pos[1] < 275 and \
                                event.pos[
                                    1] > 50:
                    print "air"
                    self.flag1 = 3
                    connection.Send(
                        {"action": "pilih", "gameid": self.gameid, "flag": self.flag1, "player": self.playerid}
                    )
            # print 'flag 1 = ', self.flag1
            # print 'flag 2 = ', self.flag2
            if (self.flag1 != None and self.flag2 != None):
                self.Load3()

    def Load3(self):
        # print 'flag 2 adalah ', self.flag2
        self.screen.fill((255, 255, 255))
        self.drawBoard3(self.flag1, self.flag2)
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.running = False

    def initGraph(self):
        self.daun = pygame.image.load("daun.png").convert_alpha()
        self.air = pygame.image.load("air.jpg").convert_alpha()
        self.api = pygame.image.load("api.jpg").convert_alpha()
        self.panel = pygame.image.load("score_panel.png").convert_alpha()
        self.red = pygame.image.load("redindicator.png").convert_alpha()
        self.green = pygame.image.load("greenindicator.png").convert_alpha()

    def drawBoard(self):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("Menunggu musuh . . .", 1, (0, 0, 0))
        self.screen.blit(label, (0, 0))

        self.screen.blit(self.daun, (0, 50))
        self.screen.blit(self.api, (230, 50))
        self.screen.blit(self.air, (465, 50))
        # self.screen.blit(self.panel, (140, 285))
        self.screen.blit(self.red, (305, 300))
        pygame.display.flip()
        # sleep(3)
        self.screen.fill((255, 255, 255))

    def drawBoard2(self):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("Pilih elemen anda . . .", 1, (0, 0, 0))
        self.screen.blit(label, (0, 0))

        self.screen.blit(self.daun, (0, 50))
        self.screen.blit(self.api, (230, 50))
        self.screen.blit(self.air, (465, 50))
        # self.screen.blit(self.panel, (140, 285))
        self.screen.blit(self.green, (305, 300))
        pygame.display.flip()

    def drawBoard3(self, flag1, flag2):
        myfont = pygame.font.SysFont("monospace", 40)
        label = myfont.render("Elemen anda: ", 1, (0, 0, 0))
        label2 = myfont.render("Elemen musuh: ", 1, (0, 0, 0))
        label3 = pygame.font.SysFont("monospace", 50).render("VS", 1, (0, 0, 0))
        self.screen.blit(label, (0, 0))
        self.screen.blit(label2, (345, 0))
        self.screen.blit(label3, (300, 150))

        if flag1 == 1:
            self.screen.blit(self.daun, (40, 50))
        elif flag1 == 2:
            self.screen.blit(self.api, (40, 50))
        elif flag1 == 3:
            self.screen.blit(self.air, (40, 50))

        if flag2 == 1:
            self.screen.blit(self.daun, (400, 50))
        elif flag2 == 2:
            self.screen.blit(self.api, (400, 50))
        elif flag2 == 3:
            self.screen.blit(self.air, (400, 50))
        self.screen.blit(self.panel, (140, 285))

        if flag1 == 1 and flag2 == 1:
            label5 = pygame.font.SysFont("monospace", 40).render("KALIAN SERI", 1, (255, 255, 255))
        elif flag1 == 1 and flag2 == 2:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU KALAH", 1, (255, 255, 255))
        elif flag1 == 1 and flag2 == 3:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU MENANG", 1, (255, 255, 255))
        elif flag1 == 2 and flag2 == 1:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU MENANG", 1, (255, 255, 255))
        elif flag1 == 2 and flag2 == 2:
            label5 = pygame.font.SysFont("monospace", 40).render("KALIAN SERI", 1, (255, 255, 255))
        elif flag1 == 2 and flag2 == 3:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU KALAH", 1, (255, 255, 255))
        elif flag1 == 3 and flag2 == 1:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU KALAH", 1, (255, 255, 255))
        elif flag1 == 3 and flag2 == 2:
            label5 = pygame.font.SysFont("monospace", 40).render("KAMU MENANG", 1, (255, 255, 255))
        elif flag1 == 3 and flag2 == 3:
            label5 = pygame.font.SysFont("monospace", 40).render("KALIAN SERI", 1, (255, 255, 255))
        self.screen.blit(label5, (150, 290))
        pygame.display.flip()


host, port = "10.151.62.99", 8000
element = Elemental(host, int(port))
while 1:
    element.Loop()
    sleep(0.001)
