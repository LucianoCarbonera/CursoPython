import forca
import adivinhacao

def escoha_jogo ():
    print("*****************")
    print("Escolha seu jogo")
    print("*****************")

    print("(1) - Adivinhacao")
    print("(2) - Forca" )
    jogo = int(input("Digite 1 ou 2 : "))

    if(jogo==1):
        print("Jogando adivinhacao")
        adivinhacao.jogar_adivinhacao()
    elif(jogo ==2):
        print("Jogando forca")
        forca.jogar_forca()

if (__name__ == "__main__"):
    escoha_jogo()
