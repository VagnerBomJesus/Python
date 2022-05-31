import math


class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.Nome = N
        self.Teste1 = T1
        self.Teste2 = T2

    def ClassifTotais(self):
        return (self.Teste1 + self.Teste2) / 2

    def ClassFinal(self):
        return math.floor((self.Teste1 + self.Teste2) / 2+0.5)

    def getNome(self):
        return self.Nome

    def getTeste1(self):
        return self.este1

    def getTeste2(self):
        return self.Teste2

    def setNome(self, N):
        self.Nome = N

    def setTeste1(self, T1):
        self.Teste1 = T1

    def setTeste2(self, T2):
        self.Teste2 = T2

    def Imprimar(self):
        print(
            f"{'Nome'}     {'Test1':^15}      {'Test2':^15}    {'Class. Final':^15}  ")
        print(f'{self.getNome():<8}      {self.getTeste1():<15}       {self.getTeste2():<15}        {self.ClassFinal():<15} \n')
