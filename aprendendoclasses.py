import pygame
from pygame.locals import *

class imagem:

	def __init__(self,diretorio,tamanho,posicao):
		self.surface = diretorio
		self.x_tamanho = tamanho[0]
		self.y_tamanho = tamanho[1]
		self.x_posicao = posicao[0]
		self.y_posicao = posicao[1]

class player:

	def __init__(self):
		self.x_posicao = 750
		self.y_posicao = 400
		self.x_tamanho = 50
		self.y_tamanho = 50
		self.surface = (r"C:\Users\Matteo Iannoni\Google Drive\INSPERMON\0.1\pokes\BellsproutFrente.png")

class tela:

	def __init__(self,tamanho):
		pygame.init()
		for event in pygame.event.get():#captura eventos na janela
			if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
				exit()
		self.screen = pygame.display.set_mode((tamanho[0], tamanho[1]), 0, 32)

	def addimg(self,imagem):
		self.screen.blit(pygame.transform.scale(pygame.image.load(imagem.surface).convert_alpha(),(imagem.x_tamanho,imagem.y_tamanho)), (imagem.x_posicao,imagem.y_posicao))
		
	def tela_update(self):
		pygame.display.update()

imagemteste = imagem(r"C:\Users\Matteo Iannoni\Google Drive\INSPERMON\Imagens\ButtMarker.png",(50,50),(100,100))
imagemteste2 = imagem(r"C:\Users\Matteo Iannoni\Google Drive\INSPERMON\Imagens\BallFull.png",(150,150),(400,200))
BG = imagem(r"C:\Users\Matteo Iannoni\Desktop\Python stuff\Grid-Sqr.gif",(2000,2000),(0,0))
jogador = player()

telinha = tela((1500,800))
keydownfix = []

while True:
	move_ticker = 0
	for event in pygame.event.get():
		print(event)
	if event.type == QUIT: #Verifica se o evento capturado é QUIT, que indica a intenção de fechar a janela pelo "x"
		exit()
	if event.type == pygame.KEYUP:
		for item in keydownfix:
			if event.key == item:
				keydownfix.remove(event.key)
		print(keydownfix)
		if 276 in keydownfix:
			jogador.x_posicao -= 10
		if 275 in keydownfix:
			jogador.x_posicao += 10
		if 273 in keydownfix:
			jogador.y_posicao -= 10
		if 274 in keydownfix:
			jogador.y_posicao += 10
	elif event.type == pygame.KEYDOWN:
		if not event.key in keydownfix:
			keydownfix.append(event.key)
		# if len(keydownfix) > 4:
		# 	keydownfix = keydownfix[1:]
		print(keydownfix)
		if 276 in keydownfix:
			jogador.x_posicao -= 10
		if 275 in keydownfix:
			jogador.x_posicao += 10
		if 273 in keydownfix:
			jogador.y_posicao -= 10
		if 274 in keydownfix:
			jogador.y_posicao += 10
	else:
		keydownfix = []
	telinha.addimg(BG)
	telinha.addimg(imagemteste)
	telinha.addimg(imagemteste2)
	telinha.addimg(jogador)
	telinha.tela_update()