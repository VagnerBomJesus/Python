
class Univ:
    def __init__(self, ent, ndisc):
        self.univ = ent
        self.pgmensal = ndisc*30

    def Paga_mensal(self):
        return self.pgmensal*1.13


class Brit:
    def __init__(self, ent, nivel):
        self.brit = ent
        if "A" <= nivel <= "C":
            self.pgmensal = 50
        else:
            self.pgmensal = 80

    def Paga_mensal(self):
        return self.pgmensal*1.13


class Ginas:
    def __init__(self, ent, h):
        self.ginas = ent
        if h in ["7-10", "14-17", "21-23", "FdS"]:
            self.pgmensal = 10
        else:
            self.pgmensal = 15

    def Paga_mensal(self):
        return self.pgmensal*1.23


class Bolsa:
    def __init__(self, nome):
        self.nome = nome

    def lernome(self):
        return self.nome
