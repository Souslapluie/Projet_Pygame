import pygame
import Rayman, capasseoupas

def Tronc() :

	# Générer fenêtre de jeu :
	pygame.display.set_caption("In Imaginary Life")  # display = affichage, set_caption = titre(s)
	screensize = screenw, screenh = 1280, 520
	screen = pygame.display.set_mode(screensize, pygame.NOFRAME | pygame.FULLSCREEN) # set_mode = affichage de la fenêtre (taille)

def Window1() :

	while running == True :

		# Application image arrière-plan ( affichage ) :

		background = pygame.image.load('../Background/LotLD.jpg').convert() # Attribution d'une image à la variable 'background'
		screen.blit(background, (0, 40))

		Img_NoRay = pygame.image.load('../Persos/Joueur/Raymans/NoRay/Noray1.png') # déclaration image du perso
		Img_Spiritomb = pygame.image.load('../Persos/Ennemy/Pokemon/spiritomb.gif')
		Pepe = pygame.image.load('../Persos/Proche/AttenteVGF.png')
		SCP = pygame.image.load('../Persos/Ennemy/²/SCP087.png')

		# blit() = afficher image,         
		#(pygame.transform.scale(NomImage, (TailleImg, tailleImg)), (PositionImg += vers droite, PosImg += vers bas)

		screen.blit(background, (0, 40))
		screen.blit(pygame.transform.scale(Img_NoRay,(90,90)), (x_Img_NoRay,y_Img_NoRay))
		screen.blit(pygame.transform.scale(Img_Spiritomb,(60,60)), (1035,355))
		screen.blit(pygame.transform.scale(Pepe,(67,195)), (850,330))
		screen.blit(pygame.transform.scale(SCP,(30,30)), (34,240))
		pygame.display.update()	
	
	pygame.quit()