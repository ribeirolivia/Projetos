import random
from time import sleep
import player


def jokenpo():
    jogadas = [1,2,3]
    pc_vence = [[1,2],[2,3],[3,1]]
    player_vence = [[1,3],[2,1],[3,2]]
    frases = ["Se aproveitam de minha nobreza","Todos os meus movimentos são friamente calculados","Empate? Suspeitei desde o princípio","Empate? Era exatamente o que eu ia dizer"]
                    
    frase1 = "\n- Finalmente te encontrei Alma Negra. Devolva já essa tal de internet!\n- Nunca, vou enterrar isso com meu tesouro.Eu só queria ver o filme do Pelé e ir embora,\nmas já que você veio me encher, teremos que lutar até a morte!\n- Então venha, seu pirata malvado, escolha suas armas! Vamos resolver isso como homens!\n"

    for char in frase1:
        sleep(0.08)
        print(char,end="",flush=True)
    sleep(1)            
    while player.chapolin.life != "" and player.almaNegra.life != "" :   
        jogo = []
        print("\nJOKENPÔ\n")
        print("[1] PEDRA")
        print("[2] PAPEL")
        print("[3] TESOURA")
        
        jogada = int(input("Faça sua escolha: "))
        while jogada not in jogadas:
            jogada = int(input("Jogue direito! Parece tonto: "))
        pc = random.randint(1,3)
        jogo.append(jogada)
        jogo.append(pc)
        jogada = 0
        print("\nJO",end="",flush=True)
        sleep(1)
        print("KEN",end="",flush=True)
        sleep(1)
        print("PÔ",end="\n\n",flush=True)
        sleep(1)
            
        if jogo in player_vence:
            for i in range(len(jogo)):
                if jogo[i] == 1:
                    jogo[i] = "PEDRA"
                elif jogo[i] == 2:
                    jogo[i] = "PAPEL"
                else:
                    jogo[i] = "TESOURA"
            print(" X ".join(jogo),"\n")
            player.almaNegra.diminuirVida()
            player.chapolin.getStatus()
            print()
            player.almaNegra.getStatus()
                
        elif jogo in pc_vence:
            for i in range(len(jogo)):
                if jogo[i] == 1:
                    jogo[i] = "PEDRA"
                elif jogo[i] == 2:
                    jogo[i] = "PAPEL"
                else:
                    jogo[i] = "TESOURA"
            print(" X ".join(jogo),"\n")
            player.chapolin.diminuirVida()
            player.chapolin.getStatus()
            print()
            player.almaNegra.getStatus()
                
                
        else:
            for i in range(len(jogo)):
                if jogo[i] == 1:
                    jogo[i] = "PEDRA"
                elif jogo[i] == 2:
                    jogo[i] = "PAPEL"
                else:
                    jogo[i] = "TESOURA"
            print(" X ".join(jogo),"\n")
            print(frases[random.randint(0,3)])
                
    if player.almaNegra.life == "":
        print("\nO Alma Negra foi derrotado. \n - Por que foi morrer justamente quando estava vivo?")
        return 1
    else:
        print("\nNosso herói foi derrotado e a culpa é sua!")
        return 0 