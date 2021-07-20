from time import sleep

class Personagem:
    def __init__(self,life,nome):
        self.life = life
        self.nome = nome
    
    def getStatus(self):
        print(self.nome,":".rjust(1),self.life)
    
class Chapolin(Personagem):    
    def __init__(self, life, nome):
        super().__init__(life, nome)
        self.estresse = 0
        self.respect = 0

    def antena(self,fator):
        if fator == "inimigo":
            print("Silêncio! Silêncio! Minhas Anteninhas de Vinil estão detectando a presença do inimigo!")
        else:
            print("Eu, o Chapolin colorado!!")
    
    def locomover(self):
        print("Siga - me os bons!")

    def panico(self):
        for i in ["Palma,", "palma. " ,"Não ", "priemos " , "cânico!!"]:
            sleep(0.5)
            print(i,end="",flush=True)
        self.estresse = 0
    
    def diminuirVida(self):
        self.life = self.life[:-1]

class AlmaNegra(Personagem):
    def __init__(self, life, nome):
        super().__init__(life, nome)

    def diminuirVida(self):
        self.life = self.life[:-2]

chapolin = Chapolin('\u2590' * 5,"Chapolin  ")
almaNegra = AlmaNegra('\u2590' * 10,"Alma Negra")


