import pygame
import Rayman, capasseoupas


def Commands() :

	pygame.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)
	while running == True :

		for event in pygame.event.get() :
			if event.type == pygame.QUIT :
				running = False

				if event.type == KEYDOWN and event.key == K_RIGHT and x_Img_NoRay + 10 < 1210 :
					x_Img_NoRay = x_Img_NoRay + 10

				if event.type == KEYDOWN and event.key == K_LEFT and x_Img_NoRay - 10 > -15 :
					x_Img_NoRay = x_Img_NoRay - 10

				if event.type == KEYDOWN and event.key == K_UP and y_Img_NoRay - 10 > 30 :
					y_Img_NoRay = y_Img_NoRay - 10

		pygame.display.update()
	pygame.quit()