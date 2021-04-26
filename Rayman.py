# Tutoriel que je suis (Graven) = https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR
# Site pour avoir pleins de sprites = https://www.spriters-resource.com/
# Tuto du poto : https://www.youtube.com/watch?v=bY9qWjzkxFc&list=PL1H1sBF1VAKXh0GR1O94UUguIxkCP3dHM

import sys, pygame                     # Alt F4 pour fermer le jeu ( pour l'instant )
from pygame import mixer
from pygame.locals import *

pygame.init()
# Création d'une classe pour le joueur :


"""  					La class ne marche pas pour l'instant, 
				le sprite du perso a été injectée en dehors de la class
				   				  Class = Objets 
"""

class Player(pygame.sprite.Sprite) :
	def __init__(self, health, max_health, attack, speed, image, rect) :
# = Insertion de différents attributs concernant la classe "Player"

		super().__init__() 
		self.health = 3
		self.max_health = 5
		self.attack = 1
		self.speed = 5
		self.image = pygame.image.load('Persos/Rayman/NoRay2.png') #Chargement de l'image du joueur
		self.rect = self.image.get_rect()
		
# Générer fenêtre de jeu :

pygame.display.set_caption("In Imaginary Life")  # display = affichage, set_caption = titre(s)
screensize = screenw, screenh = 1280, 520
screen = pygame.display.set_mode(screensize, pygame.NOFRAME | pygame.FULLSCREEN) # set_mode = affichage de la fenêtre (taille)

# Importer images : 

background = pygame.image.load('Background/LotLD.jpg').convert() # Attribution d'une image à la variable 'background'

# Application image arrière-plan ( affichage ) :
screen.blit(background, (0, 40))

Img_NoRay = pygame.image.load('Persos/Rayman/NoRay.png') # déclaration image du perso
Img_Spiritomb = pygame.image.load('Persos/Pokemon/spiritomb.gif')
Pepe = pygame.image.load('Proche/Final/AttenteVGF.png')
SCP = pygame.image.load('Background/SCP_087.png')

x_Img_NoRay = 120
y_Img_NoRay = 410

running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen True = strict minimum

mixer.music.load('Sons/Musique_LotLD.mp3')
mixer.music.play(-1)

pygame.display.update()
pygame.key.set_repeat(2, 50) # ( Délai avant de continuer mouvement, temps entre chaque déplacement)
while running == True :

	# blit() = afficher image,         
	#(pygame.transform.scale(NomImage, (TailleImg, tailleImg)), (PositionImg += vers droite, PosImg += vers bas)

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running = False

		if event.type == KEYDOWN and event.key == K_RIGHT and x_Img_NoRay + 10 < 1210 :
			x_Img_NoRay = x_Img_NoRay + 10


		if event.type == KEYDOWN and event.key == K_LEFT and x_Img_NoRay - 10 > -15 :
			x_Img_NoRay = x_Img_NoRay - 10

		if event.type == KEYDOWN and event.key == K_UP and y_Img_NoRay - 10 > 30 :
			y_Img_NoRay = y_Img_NoRay - 10

	screen.blit(background, (0, 40))
	screen.blit(pygame.transform.scale(Img_NoRay,(90,90)), (x_Img_NoRay,y_Img_NoRay))
	screen.blit(pygame.transform.scale(Img_Spiritomb,(60,60)), (1035,355))
	screen.blit(pygame.transform.scale(Pepe,(67,195)), (850,330))
	screen.blit(pygame.transform.scale(SCP,(30,30)), (34,240))
	pygame.display.update()	
			

pygame.quit()
