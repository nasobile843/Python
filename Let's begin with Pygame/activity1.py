#Import Necessary Libraries
import pygame

#Initialize Required Modules
pygame.init()

#Setup window geometry
screen = pygame.display.set_mode((400, 500))

#Create a loop to run till the game s quit by the user
done = False

while not done:

    #Clear the event que
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit

        #Make the changes visible
        pygame.display.flip()
        