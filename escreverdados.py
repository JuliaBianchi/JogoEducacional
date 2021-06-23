#Informações dos jogadores

def informacoesJogadores():
    pergunta = str(input("Informe seu nome: "))
    pergunta2 = str(input("Informe seu e-mail: "))
    
    arquivo = open("dados.txt", "a")
    arquivo.write("Nome: "+pergunta+" "+"email: "+pergunta2+"\n")
    arquivo.close()