import random

def jogar_adivinhacao():

    print("*****************")
    print("adivinhacao")
    print("*****************")

    '''
    #saber mais
    # na verdade é um pseudo ramdomico, pois ele gerar apartir de um seed, se for o mesmo seed vai gerar mesmo numero
    # normalmente usa-se os segundo atuais como seed, para gerar numeros aleatorios.
     >>> random.seed(100)
    >>> random.randrange(1, 101)
    19 '''

    # num_ramdom =  random.random() *  100
    # int(num_ramdom)  DEIXAR INTEIRO
    # round(num_ramdom)  ARREDONDA

    #num_secreto = round(random.randrange(1,101, 2)
    num_secreto = round(random.randrange(1,101))
    total_tent = 0


    '''com WHILE
    while(tentativa <= total_tent):
        chute = input("Digite o nmr: ")
        chute_int = int(chute)
        acertou = (num_secreto == chute_int)
        maior = (chute_int > num_secreto)
        menor = (chute_int < num_secreto)
    
    
        if(maior):
            print("Chute MAIOR que o valor")
            print("Voce tem {} de {}".format(tentativa, total_tent), "restantes") #interpolação
           1 print("R$ {}".format(1.59)) #interpolação usar para formatar 
           2 print("R$ {f:.2f}".format(1.59)) #interpolação usar para formatar usando apenas 2 casa apos a virgula
           3 print("R$ {:07f:.2f}".format(1.59)) #interpolação usar para formatar usando apenas 2 casa apos a virgula
           começando da posição 7 ( ou aquela qual desejar), e preencher com zeross
           4 print("R$ {:07d}".format(5)) #interpolação usar para formatar numero inteiro 
           iniciando na posição 7 ( ou a desejada), e acresentando zeros na frente
           
           #formatar data
           "Data {:02d}/{:02d}".format(9,4)
           
           # é possivel informar a posição dentro de {}, na qual ira imprimir
           print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))
            
        elif(menor):
            print("Chute MENOR que o valor")
        elif(acertou):
            print("vc digitou ", chute, "e Acertou :D!")
            break
        tentativa = tentativa + 1'''

    #com FOR
    print("Adivinhe o numero que o sistema esta armazenando e ganhe um parabens:")
    print("Qual nivel deseja?")
    print("(1) Apelão (2) Médio (3) Dificil (4) Mãe Diná")

    nivel = int(input("definido nivel: "))

    if(nivel==1):
        total_tent = 10
    elif(nivel==2):
        total_tent = 7
    elif(nivel==3):
        total_tent = 5
    else:
        total_tent = 3

    for tentativa in range(1,total_tent + 1):
        chute = input("Digite um nmr entre 1 e 100 : ")
        chute_int = int(chute)
        errou = (num_secreto != chute_int)
        acertou = (num_secreto == chute_int)
        maior = (chute_int > num_secreto)
        menor = (chute_int < num_secreto)

        if(chute_int < 1 or chute_int > 100):
            print("Voce Digitou um numero invalido")
            print("{} de {}".format(tentativa, total_tent), "tentativas")

        elif (maior):
            print("MENOS")
            print("{} de {}".format(tentativa, total_tent), "tentativas")
        elif (menor):
            print("MAIS")
            print("{} de {}".format(tentativa, total_tent), "tentativas")
        elif (acertou):
            print("*************************")
            print("vc digitou ", chute, "e Acertou :D!")
            print("*************************")
            tentar = str(input("Deseja Tentar novamente? sim ou nao?"))

            if (tentar == "sim"):
                jogar_adivinhacao()
            elif (tentar == "nao"):
                print("Fim do jogo")
    if(errou):
        print("*************************")
        print("Vc é um fracassado :C")
        print("*************************")
        tentar = str(input("Deseja Tentar novamente? sim ou nao?"))

        if(tentar=="sim"):
            jogar_adivinhacao()
        elif(tentar=="nao"):
            print("Fim do jogo")


if (__name__ == "__main__"):
    jogar_adivinhacao()
