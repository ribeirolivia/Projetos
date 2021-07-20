
import os
import player
from jokenpo import jokenpo
from time import sleep

def menu1():
    print("\nSiga-me os bons!\n")
    print("[1] COPAN")        
    print("[2] IBIRAPUERA")        
    print("[3] ESTAÇÃO DA LUZ")  
    print("[4] MASP")
    escolha = input("Escolhe aí:")
    os.system("cls")
    while escolha not in ["1","2","3","4"]:
        print("Escolha inválida")
        escolha = input("Escolhe aí:")
    if escolha == "1":
        escolha1("1")
    elif escolha =="2":
        escolha1("2")
    elif escolha == "3":
        escolha1("3")            
    else:
        escolha1("4")

def escolha1(escolha):
    print()
    if escolha == "1":
        print("Chapolin Colorado nunca se abate diante de uma porta trancada à chave. Ele logo pega a sua marreta biônica e vai procurar a chave! Depois de bater em mais de mil apartamentos dentro do bloco de concreto em formato de onda, o Gafanhoto Vermelho encontra um 'TAPA-OLHO' jogado no corredor")
        menu_vilao()
    elif escolha == "2":
        print("No maior parque da redondeza e da quadradeza, Chapolin percorre todos os museus, pistas de skate e até se joga dentro do lago, mas não encontrou nada! Ajude ele a voltar e encontrar as pistas")
        menu1()
    elif escolha == "3":
        print("Nosso herói encontra um padre que precisa de ajuda para encontrar os seus óculos que caíram em um vão muito apertado do altar. Apenas alguém com o poder de encolher pode ajudá-lo com aquilo. Chapolin está com pressa!\n")
        ajuda = input("Ele deve parar para ajudar o padre com suas pílulas de nanicolina? [S/N]:").upper()
        os.system("cls")
        while ajuda not in ["S","N"]:
            ajuda = input("Opção inválida! Digite novamente. [S/N]").upper()
        if ajuda == "S":
                print("Muito obrigado, meu filho!")
                player.chapolin.respect += 1
        menu1()
    elif escolha == "4":
        print("Abaixo do imenso vão livre do MASP, a artesã disse ter visto um homem fugindo de algo.")
        print('Ele parou para perguntar onde poderia encontrar barcos')
        menu_vilao()
    
def menu_vilao():
    opcao = 1
    while opcao == 1:
        print("\nEaí, já sabe qual vilão estamos procurando? ")
        print("\n[1] Matadouro")
        print("[2] Alma Negra")
        print("[3] Lagartixa")
        print("[4] Pança Louca")
        vilao = input()
        os.system("cls")
        while vilao not in ["1","2","3","4"]:
           print("Não seja tonto!\n1, 2, 3 ou 4?")
           vilao = input()
           os.system("cls")        
        if vilao == "2":
            print("\nIsso aí, o pirata mais temido de todos os mares, o responsável por matar o mar morto. ALMA NEGRA roubou a internet e você deve ajudar o Vermelhinho à capturá-lo. Escolha onde deve continuar procurando.")
            menu2()
            break
        else:
            opcao = int(input("Acho que não é esse!\n[1] Tentar novamente\n[2] Voltar e encontrar mais pistas\n"))
            os.system("cls")
            if opcao == 2:
                menu1()
                break
    

def menu2():
    print()
    print()
    print("\nSigam-me os bons!\n")
    print("\n[1] GUARAPIRANGA")        
    print("[2] SANTOS")        
    print("[3] RIO TIETÊ")  
    resp = input("Para onde vamos? ")
    os.system("cls")
    while resp not in ["1","2","3"]:
        print("Escolha inválida")
        resp = input("Para onde vamos? ")
        os.system("cls")
    if resp == "1":
        escolha2("1")
    elif resp =="2":
        escolha2("2")
    else:
        escolha2("3")  


def escolha2(resp):
    if resp == "1":
        print("\nNa Represa de Guarapiranga, o incansável Gafanhoto vermelho ficou chocado com o que viu...\nAquilo que um dia foi a área de lazer de muitos paulistanos, estava coberta de lixo e com algumas poucas poças de agua suja...\nPercebeu que aquele não seria o local onde encontraria o temido Alma Negra!")
        player.chapolin.panico()
        menu2()
        
    elif resp == "2":
        print("\nChegando em Santos, não pôde pensar em outra coisa: 'Assistir o filme do Pelé'.\nMas em trabalho não se brinca!\n")
        alma = "inimigo"
        player.chapolin.antena(alma)
        print("\nApós constatar que o filme do Pelé não estava mais em cartaz, lembrou - se do que realmente foi fazer em Santos:\n'Encontrar o Alma Negra e reestabelecer a Internet'\nAgora, vamos lá! Decida onde nosso herói irá continuar sua caçada.\n")
        menu_santos()
    elif resp == "3":
        print("\nChapolin resolveu começar do começo. Iniciou sua caçada em Salesopolis, na nascente. Mas quando se deu conta, já tinha se perdido e estava no rio Piracicaba.")
        print("\nAproveitam-se de minha nobreza!") 
        menu2()

def menu_santos():
    print()
    print("\n[1] MONTE SERRAT")        
    print("[2] BOQUEIRÃO")        
    print("[3] AQUÁRIO")
    print("[4] MUSEU DO PELÉ")
    santos = input()
    os.system("cls")
    while santos not in ["1","2","3","4"]:
        print("Qual a dificuldade de escolher 1,2,3 ou 4 ?")
        santos = input("\nVocê consegue!\nDecida onde nosso herói irá continuar sua caçada: ")
        os.system("cls")
    if santos == "1":
        escolha3("1")
    elif santos =="2":
        escolha3("2")
    elif santos =="3":
        escolha3("3")
    else:
        escolha3("4")

def escolha3(santos):
    if santos =="1":
        print("\nAo chegar no monte mais alto da cidade, sacou seu binóculo para ver se havia alguma movimentação suspeita\n")
        print("\n- Chapolin! Chapolin!...\n")
        turista = input("Um turista reconheceu o Chapolin, deseja falar com ele? [S/N]").lower()
        os.system("cls")
        while turista not in ["s" , "n"]:
            print("\nNão contava com a minha astúcia...\nÉ 'S' de sim ou 'N' de não! ")
            turista = input()

        if turista == "s": 
            gustavo ='\nO Vermelinho também reconheceu o turista.\n- Gustavo, você por aqui!\n- Sim, Chapolin. Estou precisando de uma ajuda, ainda não recebi meu salário em Euros, me empresta uma grana para eu comprar as coisas dessa lista ["batata","arroz","coca","presunto"].\n-Claro, toma aqui um salário de Dev Júnior na Casas Bahia, deve te ajudar.\nTime is Money! Agora preciso continuar procurando o Alma Negra. \n-Chapolin, assim você não verá nada. Seu binóculo está ao contrário!'
            for char in gustavo:
                sleep(0.08)
                print(char,end="",flush=True)

            print("\n- Suspeitei desde o princípio!\n")
            print("Vejo algo suspeito... \nAlma Negra! Ele entrou em uma construção antiga... ")
            menu_santos()
            
        else:
            print("\nNão vejo nada...\nTodos os meus movimentos são friamente calculados!\n ")
            menu_santos()
    elif santos =="2":
        print("\nQuando viu a praia do Boqueirão, resolveu dar uma volta na orla.\nEncotrou um papel amassado que dizia:\n")
        print('--'*20)
        print("\nSó de lembrar nós na Kombi no Domingo\nNosso amor era tão lindo\nNós descíamos pro Boqueirão\nA kombi quebrada lá na praia\nE você de mini-saia\nDando bola para um alemão\nO alemão de carro conversível\nEu mexendo nos fusível\nNem vi quando você me deixou...\n\nAss: MAMONAS")
        print('--'*20)
        print("\nChapolin imaginou que poderiam ser evidencias de um coração partido...\n'Nunca abuse de um homem caído, afinal, ele pode se levantar...\n")
        menu_santos()
    elif santos == "3":
        print("\nNa entrada do Aquário, o incrível Gafanhoto Vermelho resolveu perguntar no guichê se alguém havia visto o temido Pirata Alma Negra.\nUma senhora de idade avançada, contou que enquanto fazia sua caminhada diária, ouviu um homem dizendo ter torturado seu capanga, fazendo-o assistir programa de políticos na televisão pelo resto de seus dias!\n-'Que malvado! Ele foi em direção ao Museu!'\n")
        menu_santos()
    elif santos =="4":
        print("\nChapolin ficou encantado ao entrar no museu do Pelé...\n")
        alma = "inimigo"
        player.chapolin.antena(alma)
        final(jokenpo())
        

def final(jokenpo):
    if jokenpo == 1:
        print("Misteriosamente, Alma Negra se transforma em um fantasma e nenhum golpe do nosso pequeno gafanhoto pode atingí-lo\n")

        if player.chapolin.respect == 1:
            frase1 = "O nosso herói está deseperado sem saber o que fazer e grita no meio do museu\n- Oh e agora quem poderá me defender?\n\nDe repente surge alguém no horizonte... \nMontado em uma bicicleta em alta velocidade se atira contra os vidros do museu o pequeno senhor que o Chapolin ajudou em São Paulo.\n- Eu sou o Padre Jaiminho, pra acabar com espíritos você nunca está sozinho!\n O incrível Jaiminho Carteiro/Padre realiza um exorcismo (devagar para evitar a fadiga) e o fantasma do Alma Negra desaparece instantaneamente.\n ...Chapolin e Jaiminho viajam para Tangamandápio e reinstalam a internet, transformando a cidade no novo Vale do Silício"
            for char in frase1:
                sleep(0.08)
                print(char,end="",flush=True)

            frase2 = "\nEi você que está aí jogando...\nIsso foi um sonho, uma alucinação ou um trabalho de conclusão de módulo?\n\nNunca mais tente fumar um gafanhoto vermelho.\n\nSaia dessa cadeira e vá procurar o PROERD."

            for char in frase2:
                sleep(0.08)
                print(char,end="",flush=True)
            sleep(3)    

            print("\n\033[1;33;40mPROERD é o programa, PROERD é a solução.\033[0m\n")  

        else:
            frase1 = "\nDesesperado e sem saber o que fazer, Chapolin cai no mar e usa sua super força para fugir nadando até Acapulco.\n\nJá diz o ditado: Fazer alguém sem olhar o bem que tem… Não… Fazer o bem sem olhar o que tem alguém… É mais ou menos isso."
            for char in frase1:
                sleep(0.1)
                print(char,end="",flush=True)
            sleep(1)    
            print("\n\033[1;31;40mO MUNDO QUE SE VIRE SEM A INTERNET\033[0m\n")
            sleep(3)
            frase2 = "\nEi você que está aí jogando...\nIsso foi um sonho, uma alucinação ou um trabalho de conclusão de módulo?\n\nNunca mais tente fumar um gafanhoto vermelho.\n\nSaia dessa cadeira e vá procurar o PROERD."

            for char in frase2:
                sleep(0.08)
                print(char,end="",flush=True)

            print("\n\033[1;33;40mPROERD é o programa, PROERD é a solução.\033[0m\n") 
    else:
        frase1 = "Na incapacidade de ganhar um Jokenpo, Chapolin será assombrado pelo resto da vida..."

        for char in frase1:
                sleep(0.08)
                print(char,end="",flush=True)

        frase2 = "\nEi você que está aí jogando...\nIsso foi um sonho, uma alucinação ou um trabalho de conclusão de módulo?\n\nNunca mais tente fumar um gafanhoto vermelho.\n\nSaia dessa cadeira e vá procurar o PROERD."

        for char in frase2:
            sleep(0.08)
            print(char,end="",flush=True)

        print("\n\033[1;33;40mPROERD é o programa, PROERD é a solução.\033[0m\n")            
    
    sleep(2)
    print("Keanu Reeves como 'Padre Jaiminho'")
    print('Chapolin como "Chapolin"')
    print('Seu madruga como "Alma negra"')
    print('Gustavo como "Turista"')
    print('Palmeiras não tem "mundial"')
    print()
    sleep(2)
    print("Desenvolvido por:")
    print("Livia Ribeiro como 'Alessandra Negrini'")
    print("Jobson Brito como 'O Dramático'")
    print("Vander Xavier como 'Roteirista'")    
              

