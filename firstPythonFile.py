#Do not forget to "Debug" the file so that latest changes are added
import pygame  
  
pygame.init()  
screen = pygame.display.set_mode((400,500))  
done = False  
x = 10
y = 10


while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True

        #Do logical updates here
        color = (255,0,0)
        x += 1


        #Render graphics here. Display frames per seconds
        #count minutes and seconds. Draw game objects
        pygame.draw.rect(screen, color, pygame.Rect(x,y,10,10))            
        pygame.display.flip()  