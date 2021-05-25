# Tutoriel que je suis (Graven) = https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR
# Site pour avoir pleins de sprites = https://www.spriters-resource.com/ 
# Tuto du poto : https://www.youtube.com/watch?v=bY9qWjzkxFc&list=PL1H1sBF1VAKXh0GR1O94UUguIxkCP3dHM

import sys, pygame, Gameplay
from pygame import mixer
from pygame.locals import *

pygame.init()
Gameplay.Commands()
Visual.Tronc()
Visual.Window1()
Musiques.LotLDTheme()

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
		self.image = pygame.image.load('../Persos/Joueur/Raymans/NoRay/Noray1.png') #Chargement de l'image du joueur
		self.rect = self.image.get_rect()

running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen True = strict minimum
