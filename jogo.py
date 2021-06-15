import pygame


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

#cores
preto = (0,0,0)
branco = (255,255,255)

#configurações do fundo
fundo = pygame.image.load("assets/saladeaula1.jpg")

#config - ator
ator = pygame.image.load("assets/ator.png")


while True:
    #início - verificação de interação com o usuário
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    #fim - verificação de interação com o usuário

    display.blit(fundo, (0,0)) #inserir imagem na tela
    display.blit(ator, (400,300))
    pygame.display.update() 
    fps.tick(60)

