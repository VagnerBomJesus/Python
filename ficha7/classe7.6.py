import math
from ficha7.ex01 import *


class EstudanteInf():
    def __init__(self, N, T1, T2):
        self.Nome = N
        self.Teste1 = T1
        self.Teste2 = T2

    def ClassFinal(self):
        return math.floor((self.Teste1 + self.Teste2) / 2+0.5)


def menu():
    E = EstudanteInf("Ana Paiva", 14, 16)
    print(f"{E.Nome} teve a classif. final de {E.ClassFinal()} valores: ")

    E.Imprimar()


menu()
