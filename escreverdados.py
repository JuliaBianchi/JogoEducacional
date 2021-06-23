#Informações dos jogadores

def informacoesJogadores(pergunta,pergunta2):
    pergunta = str(input("Informe seu nome: "))
    pergunta2 = str(input("Informe seu e-mail: "))


    arquivo = open("dados.txt", "a")
    arquivo.write(pergunta+" " + pergunta2 + "\n")
    arquivo.close()