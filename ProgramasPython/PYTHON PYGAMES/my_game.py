import pygame, sys, os, time, random
from pygame.locals import*

#Inicializando modulo pygame
pygame.init()

#resolucao
display_width = 800
display_height = 600

#Cores RGB
black = (0, 0, 0)
white = (255, 255, 255)
red   = (255, 0, 0)
green = (0, 255, 0)
blue  = (0, 0, 255)

colors = [black, red, green, blue]

window = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("CAR GAME")
clock = pygame.time.Clock()

car = pygame.image.load("carro.jpg")
carro_width = 80
car.set_colorkey((255, 255, 255))

def objetos (objeto_x, objeto_y,  objeto_w, objeto_h, color):
	pygame.draw.rect(window, color, [objeto_x, objeto_y, objeto_w, objeto_h])

def pontos_desvios(count):
	font = pygame.font.SysFont(None, 40)
	text = font.render ("SCORE: " + str(count), True, black)

	window.blit (text, (0, 0))

def carro(x, y):
	window.blit(car, (x,y))

def text_objects (text, font):
	textSurface = font.render(text, True, blue)

	return textSurface, textSurface.get_rect()

def message_display (text):
	largeText = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = text_objects (text, largeText)
	TextRect.center = ((display_width/2), (display_height/2))
	window.blit(TextSurf, TextRect)

	pygame.display.update()

	time.sleep(2)

	game()

def crash():
	message_display ("Voce bateu!")

def game():
	
	#Posicao inicial do carro
	carro_x = 330
	carro_y = 476

	#Mudanca na posicao do carro
	change_x = 0

	#Posicao objeto
	object_x = random.randint(0, display_width)
	object_y = -600
	object_speed = 7
	object_width = 100
	object_height = 100

	#Poder manter a tecla pressionada, SETAR em 0 ou 1
	pygame.key.set_repeat(1)

	color = random.choice(colors)

	desvios = 0
	points = 1
	y_speed = 0.1

	running = True

	while running:
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.display.quit()
				sys.exit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					change_x = -5

				if event.key == pygame.K_RIGHT:
					if carro_x<718: 
						change_x = 10

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					change_x = 0

		carro_x += change_x

		window.fill(white)

		# objetos (objeto_x, objeto_y,  objeto_w, objeto_h, color):
		objetos (object_x, object_y, object_width, object_height, color)
		object_y += object_speed
		carro(carro_x, carro_y)
		pontos_desvios (desvios)

		if carro_y < object_y + object_height:
			if carro_x > object_x and carro_x < object_x + object_width or carro_x+carro_width > object_x and carro_x + carro_width < object_x + object_width:
				crash()	

		if carro_x > display_width - carro_width or carro_x<0:
			crash()

		if object_y > display_height:
			color = random.choice(colors)
			object_x = random.randint(0, display_width)
			object_y = 0 - object_height
			desvios += points
			object_speed += y_speed
			points+=1

		pygame.display.update()

		clock.tick(60)


game()
