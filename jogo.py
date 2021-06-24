import pygame
import time
import random
from pygame.locals import *
from escreverdados import informacoesJogadores

#Armazenar os dados
informacoesJogadores()

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
erros = 0

#pegas a posição do mouse
x,y = pygame.mouse.get_pos()
print(x)
print(y)

#Placar de pontos
def escrevendoPlacar(pontos):
    font = pygame.font.SysFont(None, 45)
    texto = font.render("Pontos: "+str(pontos), True, branco)
    texto2 = font.render("Erros: "+str(erros), True, branco)
    display.blit(texto, (800, 200))
    display.blit(texto2, (800, 250))

def gameOver():
    if erros == 5:
        font = pygame.font.SysFont(None, 45)
        texto = font.render("Você Perdeu :( "+str(erros)+" erros! ", True, branco)
        display.blit(texto, (800, 300))
        pygame.display.update() 
        time.sleep(3)
        pygame.quit()
        quit()


def jogo():
    global erros
    pygame.mixer.music.load("assets/somdefundo.mp3")
    pygame.mixer.music.play(-1)
    fundo = pygame.image.load("assets/saladeaula1.jpg")
    ator = pygame.image.load("assets/ator.png")
    mensagem = pygame.image.load("assets/fala.png")
    logo = pygame.image.load("assets/cc.png")
    pontos = 0
    velocidade = 3
    posicaoYbalao = 600
    posicaoXbalao = largura * 0.45
    larguraBalao = 90
    alturaBalao = 212
    listaPosicao = [random.randrange(50),random.randrange(55,200),random.randrange(300,400),random.randrange(600,700),random.randrange(800,900),random.randrange(1000,1110),random.randrange(100,260)]
    listaVelocidade = [2,1,2,1,2,1,2]
    listaYbaloes = [720,720,720,720,720,720,720]
    estouroSound = pygame.mixer.Sound("assets/estouro.wav")

    #imagens - Balões
    vogalA =  pygame.image.load("assets/a.png")
    vogalE =  pygame.image.load("assets/e.png")
    vogalI =  pygame.image.load("assets/i.png")
    vogalO =  pygame.image.load("assets/o.png")
    vogalU =  pygame.image.load("assets/u.png")
    balaoLaranja = pygame.image.load("assets/balaolaranja.png")
    balaoVerde = pygame.image.load("assets/balaoverde.png")

    while True:
        #início - verificação de interação com o usuário
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit() 
            #Pegar a posição do Balão
            if evento.type == MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                for i in range(0,4):
                    if x >= listaPosicao[i] and x <= listaPosicao[i] +80:
                        if y >= listaYbaloes[i] and y <= listaYbaloes[i]+100:
                            listaYbaloes[i] = 720
                            pygame.mixer.Sound.play(estouroSound)
                            pontos += 1
                for i in range(4,6):
                    if x >= listaPosicao[i] and x <= listaPosicao[i] +80:
                        if y >= listaYbaloes[i] and y <= listaYbaloes[i]+100:
                            listaYbaloes[i] = 720
                            erros = erros + 1

                if x >= posicaoXbalao and x <= posicaoXbalao +80:
                    if y >= posicaoYbalao and y <= posicaoYbalao+100:
                        posicaoYbalao = 720
                        pygame.mixer.Sound.play(estouroSound)
                        pontos += 1
        #fim - verificação de interação com o usuário

        display.blit(fundo, (0,0)) #inserir imagem na tela
        display.blit(ator, (200,150))
        display.blit(mensagem, (390,50))
        display.blit(logo,(937,420))

        escrevendoPlacar(pontos)
        gameOver()



        #Balões subindo
        listaYbaloes[0] = listaYbaloes[0] - listaVelocidade[0]
        listaYbaloes[1] = listaYbaloes[1] - listaVelocidade[1]
        listaYbaloes[2] = listaYbaloes[2] - listaVelocidade[2]
        listaYbaloes[3] = listaYbaloes[3] - listaVelocidade[3]
        listaYbaloes[4] = listaYbaloes[4] - listaVelocidade[4]
        listaYbaloes[5] = listaYbaloes[5] - listaVelocidade[5]
        listaYbaloes[6] = listaYbaloes[6] - listaVelocidade[6]
        posicaoYbalao = posicaoYbalao - listaVelocidade[3]

        if posicaoYbalao <= -200:
            posicaoYbalao = 600
            posicaoXbalao = random.randrange(0, largura-50)
        for i in range(0,7):
            if listaYbaloes [i] <= -200:
                listaYbaloes[i] = 600
                listaPosicao[i] = random.randrange(0, largura)   

        display.blit(vogalA, (posicaoXbalao, posicaoYbalao))
        display.blit(vogalE, (listaPosicao[0], listaYbaloes[0]))
        display.blit(vogalI, (listaPosicao[1], listaYbaloes[1]))
        display.blit(vogalU, (listaPosicao[2], listaYbaloes[2]))
        display.blit(vogalO, (listaPosicao[3], listaYbaloes[3]))
        display.blit(balaoVerde, (listaPosicao[4], listaYbaloes[4]))
        display.blit(balaoLaranja, (listaPosicao[5], listaYbaloes[5]))
        pygame.display.update() 
        fps.tick(60)
jogo()