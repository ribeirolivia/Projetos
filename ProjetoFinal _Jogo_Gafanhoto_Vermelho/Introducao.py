import os
import random
from time import sleep
from menus import menu1


cores = {"reset_color":"\033[0m","red":"\033[1;31;40m","green":"\033[1;32;40m","yellow":"\033[1;33;40m","blue" : "\033[1;34;40m","magenta":"\033[1;35;40m","cyan":"\033[1;36;40m"}

def titulo():
    print("\033[1;31;40m                                  O      O        \033[0m")
    print("\033[1;31;40m                                   \    /         \033[0m")
    print("\033[1;31;40m                                    \  /          \033[0m")
    print("\033[1;31;40m __     __   __   __  __  _   _ _  _  __  ___  __ \033[0m")
    print("\033[1;31;40m|  |   | _  |__| |__ |__| |\  | |__| |  |  |  |  |\033[0m")
    print("\033[1;31;40m|  |   |  | |  | |   |  | | \ | |  | |  |  |  |  |\033[0m")
    print("\033[1;31;40m|__|   |__| |  | |   |  | |  \| |  | |__|  |  |__|\033[0m")
    print()
    print("\033[1;31;40m      _    _  __   __  _  _  __ _   _  _  __      \033[0m")
    print("\033[1;31;40m      \    / |__  |__| |\/| |__ |   |__| |  |     \033[0m")
    print("\033[1;31;40m       \  /  |    |\   |  | |   |   |  | |  |     \033[0m")
    print("\033[1;31;40m        \/   |__  | \  |  | |__ |__ |  | |__|     \033[0m")
    print("\nCriamos uma barra de carregamento para te deixar ansioso,\nnão tem nada pra carregar, mas adoramos o efeito:")
    print()
    for char in "\u2590" * 48:
        sleep(0.5)
        print(random.choice(list(cores.values()))+char+cores["reset_color"],end="",flush=True)


def introducao():
    
    
    
    
    titulo()

    parte1 =  "\n\nSão Paulo... 2025.\nAs pessoas andam sem rumo...\nNão sabem mais chegar em suas casas, nem os telefones de seus amigos...\nPerderam a noção de quais são os melhores bares, não conseguem mais avaliar mal os restaurantes,\npararam de dançar por não ter onde postar, deixaram de fotografar seus pratos...\ne a pior catástrofe de todas:\nHá tempos não vemos nenhum #tbt de 2015 daquelas viagens, tatuagens novas e mudanças de cabelo.\n\n \033[1;31;40m A INTERNET FOI ROUBADA! \033[0m"


    parte2 ="\n\033[1;33;40m (AVISO:  ESSE JOGO VEIO DO FUTURO ATÉ VOCÊ, AJUDE O NOSSO HERÓI A FAZER AS ESCOLHAS CERTAS E SALVAR A INTERNET PARA QUE VOCÊ POSSA CONTINUAR COMPARTILHANDO SEUS CÓDIGOS DO KWAI!) \033[0m"

    for char in parte1:
        sleep(0.1)
        print(char,end="",flush=True)

    print("\n",parte2)    




def menu_intro():

    chamada = "\nEEEEEEEEEOOOOOOOUUUUUUUUUU!!!\n\nDe repente surge o Polegar Vermelho, direto de um lugar qualquer no tempo espaço para a grande São Paulo.\nEle não sabe bem o que aconteceu e nem muito bem onde está,por isso você deve guiá-lo pela cidade\npara encontrar as pistas corretas e chegar ao vilão que roubou a internet."


    print("\nDiga alguma coisa e invoque o nosso herói:\n")
    print("[1] Oh e agora quem poderá nos defender?")        
    print("[2] Terra, fogo, vento, água, coração!")        
    print("[3] Se você não conhece nenhuma das frases acima, desligue o computador, geração Z")  
    print()
    
    escolha = input("Escolhe aí:")
    os.system("cls")
    while escolha not in ["1","2","3"]:
        print("Qual a dificuldade de escolher 1,2 ou 3 ?")
        escolha = input("Escolhe aí:")
        os.system("cls")
    if escolha == "1":
        print(chamada)
        menu1()
    elif escolha =="2":
        print("Pegadinha do Malandro! A gente jamais faria um jogo do Capitão Planeta, esse desenho era muito chato!")
        escolha = input("\nEscolhe outro aí:")
        while escolha not in ["1","3"]:
            escolha = input("\nEscolhe OUTRO!:")
        if escolha == "1":
            print(chamada)
            menu1()         
        else:
            print("Obrigado por não jogar.")
            
    else:
        print("Obrigado por não jogar!")
        

