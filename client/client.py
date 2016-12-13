import pygame
#from threading import Thread


class TicTacGame():
	def __init__(self):
		pass
		#membuat kotak
		pygame.init()
		self.screen = pygame.display.set_mode((645, 710))
		pygame.display.set_caption("Tic Tac Toe")
		self.clock = pygame.time.Clock()

		#inisialisasi
		self.running = True

		#inisialisasi board 10x10
		#garis
		self.boardh = [[False for x in range(10)] for y in range(11)]
		self.boardw = [[False for x in range(11)] for y in range(10)]
		#kotak
		self.kotak = [[False for x in range(10)] for y in range(10)]

		#inisialisasi posisi client ketika klik kotak
		self.xpos = -1
		self.ypos = -1

		#membuat 60 fps
		self.clock.tick(60)
		self.screen.fill(0)

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
		self.normallinew = pygame.image.load("normalline.png").convert_alpha()
		self.normallineh = pygame.transform.rotate(pygame.image.load("normalline.png"), -90).convert_alpha()
		self.separators = pygame.image.load("separators.png").convert_alpha()

	def drawBoard(self):
		for x in range(10):
			for y in range(11):
				if not self.boardh[y][x]:
					self.screen.blit(self.normallineh, [(x)*64+5, (y)*64])
		for x in range(11):
			for y in range(10):
				if not self.boardw[y][x]:
					self.screen.blit(self.normallinew, [(x)*64, (y)*64+5])
		for x in range(11):
			for y in range(11):
				self.screen.blit(self.separators, [x*64, y*64])
		

tictac = TicTacGame()