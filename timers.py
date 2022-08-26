import pygame

pygame.init()

screen = pygame.display.set_mode((500,600))

GREY = (100,200,50)

while True:
	screen.fill(GREY)

	for event in pygame.event.get():
		pass
	pygame.display.flip()

pygame.quit()
