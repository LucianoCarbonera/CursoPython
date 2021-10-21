import random

def jogar_forca():
    msg_abertura()
    escrita_palavra_secreta()
    palavra_secreta = leitura_palavra_secreta()
    letras_acertadas = carrega_palavra_secreta(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas, palavra_secreta)

        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(7 - erros))
            desenha_forca(erros)

        enforcou = erros ==7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("Fim do jogo.")

def msg_abertura():
    print("*****************")
    print("Forca")
    print("*****************")
    print("Tema: Frutas")

def escrita_palavra_secreta():
    # a adicionar #w substituir #r ler
    # comando with usa a funcao open, nao sendo mais necessario fechar o arquivo .close()
   with open("palavras.txt", "w") as arquivo:
        arquivo.write("banana\n")
        arquivo.write("morango\nmelancia\npessego\nabacaxi\nmelao\nabacate\n")
        # arquivo.close()  boa pratica fechar o arquivo

def leitura_palavra_secreta():
    # comando with usa a funcao open, nao sendo mais necessario fechar o arquivo .close()
    with open("palavras.txt", "r") as arquivo:
        # readline() ler uma unica linha do txt
        palavras = []
        for linha in arquivo:
            linha = linha.strip() #armazenar a palavra na lista sem caracteres especiais neste caso o \n
            palavras.append(linha) #adicionar na nova variavel palavras cada linha do palavras.txt percorrida no for
    # de forma randomica escolhe o indice da palavra secreta
    indice_palavra = random.randrange(0,len(palavras))
    palavra_secreta = palavras[indice_palavra].upper()
    return palavra_secreta

def carrega_palavra_secreta(palavras):
    # forma com FOR normal para incrementar o _ na lista
    # palavra_secreta = "banana".upper() #forma fixa
    # for letra in palavra_secreta:
    #   letras_acertadas.append("_")
    return ["_" for letra in palavras]

def num_tentativas():
    erros = 6
    return erros

def pede_chute():
    input("Letra:")
    chute = chute.strip().upper()
    # Strip()Método que retorna uma copia da string removendo caracteres do inicio e do fim(espaços)
    return chute;

def marca_chute_correto(chute,letras_acertadas, palavra_secreta):
    posicao = 1
    for letra in palavra_secreta:  # PERCORRE A STRING
        if (chute == letra):
            letras_acertadas[posicao - 1] = letra  # ARMAZENA NA POSIÇÃO ATUAL DA STRING
            # print("Enconrei a letra {} nao posicao {}".format(letra, posicao))
        posicao += 1

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



if (__name__ == "__main__"):
    jogar_forca()


# palavra.find("b")

# []  lista
# () tuple

# {} set
#Para adicionar um elemento a um set devemos chamar a função add (invés da append):
#colecao.add(44455566677)

#DICIONARY
#instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
#instrutores['Flavio']