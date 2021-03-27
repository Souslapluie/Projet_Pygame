# Tutoriel que je suis (Graven) = https://www.youtube.com/watch?v=8J8wWxbAdFg&list=PLMS9Cy4Enq5KsM7GJ4LHnlBQKTQBV8kaR

import pygame 

pygame.init()

# Générer fenêtre de jeu

pygame.display.set_caption("Rayman Rev1val")  # display = affichage, set_caption = titre(s)
screen = pygame.display.set_mode((1080, 720)) # set_mode = affichage de la fenêtre (taille)

# Importer images : 

background = pygame.image.load('Raymages/Rayman1.5.webp') # Attribution d'une image à la variable 'background'

running = True # running = Nom de la boucle while ? While ne marche pas toute seule, booléen strict minimum

while running == True :

	# Application image arrière-plan
	screen.blit(background, (0, 0))

	#MAJ ecran
	pygame.display.flip()

	for event in pygame.event.get() :
		if event.type == pygame.QUIT :
			running == False
			pygame.quit()   # Ferme la fenêtre lorsqu'on clique sur la croix (croix marche pas sans cette ligne)

  
   
