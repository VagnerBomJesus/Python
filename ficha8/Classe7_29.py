from telnetlib import SE


class SNS():
    def __init__(self, NUSNS, NISS, Centro):
        self.__NUSNS = NUSNS
        self.__NISS = NISS
        self.__CSaude = Centro

    def SerSaude(self):
        return f"{self.__NUSNS}-{self.__NISS} {self.__CSaude:10}"

    def getCSaude(self):
        return self.__CSaude


class SegSaude():
    AnoCorrente = 2022

    def __init__(self, Comp, Apol, Nasc):
        self.__Comp = Comp
        self.__Apol = Apol
        self.__Nasc = Nasc

    def Valor(self):
        return 10+3*(max(SegSaude.AnoCorrente-self.__Nasc-65, 0))

    def getComp(self):
        return self.__Comp

    def getApol(self):
        return self.__Apol


class Utente(SNS, SegSaude):
    def __init__(self, t):
        SNS.__init__(self, t[0], t[1], t[2])
        SegSaude.__init__(self, t[3], t[4], t[5])
        self.__Nome = t[6]

    def getNome(self):
        return self.__Nome


class ListaCentrosSeguros1():
    def __init__(self, k):
        self.__a = k[2]
        self.__b = k[3]

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b
