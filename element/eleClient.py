import pygame
#from threading import Thread


class Elemental():
	def __init__(self):
		#membuat kotak
		pygame.init()
		self.screen = pygame.display.set_mode((690, 400))
		pygame.display.set_caption("Elemental Fight")
		self.clock = pygame.time.Clock()

		#inisialisasi
		self.running = True

		#inisialisasi posisi client ketika klik element
		self.xpos = -1
		self.ypos = -1

		#membuat 60 fps
		self.clock.tick(60)

		#warna bg
		self.screen.fill((255, 255, 255))

		#inisialisasi objek
		self.initGraph()

		#layar menunggu
		#if self.running:
		#	thread = Thread(target = self.tunggu())
		#	thread.start()

		#membuat tampilan permainan
		self.drawBoard()
		
		#screen update
		pygame.display.flip()

		#menunggu musuh masuk
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()

	def tunggu(self):
		pygame.display.flip() 

	def initGraph(self):
		self.daun = pygame.image.load("daun.png").convert_alpha()
		self.air = pygame.image.load("air.jpg").convert_alpha()
		self.api = pygame.image.load("api.jpg").convert_alpha()
		#self.panel = pygame.image.load("score_panel.png").convert_alpha()
		self.red = pygame.image.load("redindicator.png").convert_alpha()		
		self.green = pygame.image.load("greenindicator.png").convert_alpha()
	def drawBoard(self):
		myfont = pygame.font.SysFont("monospace", 40)
		label = myfont.render("Menunggu musuh . . .", 1, (0,0,0))
		self.screen.blit(label, (0, 0))

		self.screen.blit(self.daun, (0,50))
		self.screen.blit(self.api, (230,50))
		self.screen.blit(self.air, (465,50))
		#self.screen.blit(self.panel, (140, 285))
		self.screen.blit(self.red, (305, 300))
		
element = Elemental()
#while 1:
#	if tictac.update() == 1:
#		break
#tictac.finished()
