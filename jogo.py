import pygame
import time
import random

#iniciando o pygame
pygame.init()

#configurando o display
largura = 1280
altura = 720
display = pygame.display.set_mode((largura,altura))
fps = pygame.time.Clock()

#características do jogo
pygame.display.set_caption("O Mundo Mágico das Letras")
icone = pygame.image.load("assets/mestre-dos-magos.jpg")
pygame.display.set_icon(icone)

#variaveis
preto = (0,0,0)
branco = (255,255,255)
fundo = pygame.image.load("assets/saladeaula1.jpg")
ator = pygame.image.load("assets/ator.png")
fala = pygame.image.load("assets/fala.png")
vogalA =  pygame.image.load("assets/balaoA.png")
vogalE =  pygame.image.load("assets/balaoE.png")
vogalI =  pygame.image.load("assets/balaoI.png")
vogalO =  pygame.image.load("assets/balaoO.png")
vogalU =  pygame.image.load("assets/balaoU.png")

#Pegar a posição do mouse
x,y = pygame.mouse.get_pos()
print(x)
print(y)

while True:
    #início - verificação de interação com o usuário
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    #fim - verificação de interação com o usuário
    
    #config da tela
    display.blit(fundo, (0,0)) #inserir imagem na tela
    display.blit(ator, (200,150))
    display.blit(fala, (350,50))
    pygame.display.update() 
    fps.tick(60)

