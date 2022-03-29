import pygame 
import sys
pygame.init()
num = 0
num2 = 0
font = pygame.font.SysFont('Serif', 35)
x = 350
y = 360
font2 = pygame.font.SysFont('Serif', 20)
screen = pygame.display.set_mode((720, 720))
run = True 
while run:
	screen.fill((0, 255, 0))
	# Shadow
	
	
	pygame.draw.circle (screen, (0, 100, 0), (365, 385), 100)
	pygame.draw.circle (screen, (255, 255, 255), (360, 380), 100)
	
	pygame.draw.circle (screen, (255, 0, 0), (360, 380), 80)
	k = str(num)
	n = str(num2)
	
	text = font.render(k, True, (0, 255, 0))
	century = font2.render(n, True, (0, 0, 0))
	screen.blit(text, (x, y))
	screen.blit (century, (20, 20))
	for event in pygame.event.get():
		if event.type == pygame.FINGERUP:
			num+=1
			
			if num == 10:
				x -= 10
			if  num % 100 == 0:
				x -= 10
				num2 += 1
				num = 0
		if num == 0:
				x = 350
	
	pygame.display.update ()
