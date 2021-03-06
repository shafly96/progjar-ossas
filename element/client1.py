import pygame
from time import sleep, time

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

		#self.tunggu()

		#warna bg
		self.screen.fill((255, 255, 255))

		#inisialisasi objek
		self.initGraph()

		#membuat tampilan permainan
		self.drawBoard()

		self.drawBoard2()

		#running program
		flag1 = 0
		flag2 = 0
		x=0
		while self.running:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
				#elif event.type == pygame.MOUSEBUTTONDOWN:
					#print "koordinat = (%d, %d)"%event.pos
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] < 228 and event.pos[1] < 275 and event.pos[1] > 50:
					print "daun"
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 227 and event.pos[0] < 463 and event.pos[1] < 275 and event.pos[1] > 50:
					print "api"
				elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] > 462 and event.pos[1] < 275 and event.pos[1] > 50:
					print "air"

	def initGraph(self):
		self.daun = pygame.image.load("daun.png").convert_alpha()
		self.air = pygame.image.load("air.jpg").convert_alpha()
		self.api = pygame.image.load("api.jpg").convert_alpha()
		self.panel = pygame.image.load("score_panel.png").convert_alpha()
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
		pygame.display.flip()
		sleep(3)
		self.screen.fill((255,255,255))

	def drawBoard2(self):
		myfont = pygame.font.SysFont("monospace", 40)
		label = myfont.render("Pilih elemen anda . . .", 1, (0,0,0))
		self.screen.blit(label, (0, 0))

		self.screen.blit(self.daun, (0,50))
		self.screen.blit(self.api, (230,50))
		self.screen.blit(self.air, (465,50))
		#self.screen.blit(self.panel, (140, 285))
		self.screen.blit(self.green, (305, 300))
		pygame.display.flip()

element = Elemental()