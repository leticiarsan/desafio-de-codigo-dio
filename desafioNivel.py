


class Heroi():
    def __init__(self, nome, xp):
        self.__nome = nome
        self.__xp = xp
        self.__nivel = None
    def setNome(self, novoNome):
        self.__nome = novoNome
    def getNome(self):
        return self.__nome
    def setXp(self, novoXp):
        self._Game__xp = novoXp
    def getXp(self):
        return self.__xp
    def aumentaXp(self):
        self.__xp += 1000
    def getNivel(self):
        if self.__xp<=1000:
            self.__nivel = "Ferro"
        elif self.__xp<=2000:
            self.__nivel = "Bronze"
        elif self.__xp <= 5000:
            self.__nivel = "Prata"
        elif self.__xp <= 7000:
            self.__nivel = "Ouro"
        elif self.__xp <= 8000:
            self.__nivel = "Platina"
        elif self.__xp <= 9000:
            self.__nivel = "Ascendente"
        elif self.__xp <= 10000:
            self.__nivel = "Imortal"
        elif self.__xp > 10000:
            self.__nivel = "Radiante"
        return self.__nivel
    def dadosHeroi(self):
        print(f"O Heroi de nome {self.getNome()} esta no nivel de {self.getNivel()} com XP igual a {self.getXp()}")

heroi1 = Heroi("Shadow", 1000)
heroi2 = Heroi("IceBoss", 6840)


heroi1.dadosHeroi()
heroi1.aumentaXp()
heroi1.dadosHeroi()
heroi1.aumentaXp()
heroi1.aumentaXp()
heroi1.dadosHeroi()
print("_____________")
heroi2.dadosHeroi()
heroi2.aumentaXp()
heroi2.dadosHeroi()
heroi2.aumentaXp()
heroi2.aumentaXp()
heroi2.dadosHeroi()