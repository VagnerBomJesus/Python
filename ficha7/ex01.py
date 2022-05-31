'''
import math


class estudateInf():
    def __init__(self, N, T1, T2):
        self.__Nome = N
        self.__Teste1 = T1
        self.__Teste2 = T2

    def ClassifTotais(self):
        return (self.__Teste1 + self.__Teste2) / 2

    def ClassFinal(self):
        return math.floor((self.__Teste1 + self.__Teste2) / 2+0.5)

    def getNome(self):
        return self.__Nome

    def getTeste1(self):
        return self.__Teste1

    def getTeste2(self):
        return self.__Teste2

    def setNome(self, N):
        self.__Nome = N

    def setTeste1(self, T1):
        self.__Teste1 = T1

    def setTeste2(self, T2):
        self.__Teste2 = T2

    def Imprimar(self):
        print(
            f"{'Nome'}     {'Test1':^15}      {'Test2':^15}    {'Class. Final':^15}  ")
        print(f'{self.getNome():<8}      {self.getTeste1():<15}       {self.getTeste2():<15}        {self.ClassFinal():<15} \n')


def menu():
    e = estudateInf("Vagner", 19, 14)
    print('\n 7_1')
    print(f'{e.getNome()} teve a classif. final de {e.ClassifTotais()} valores \n')
    print('\n 7_1_Math')
    print(f'{e.getNome()} teve a classif. final de {e.ClassFinal()} valores')

    print('\n 7_2')
    print(f"{'Nome'}     {'Test1':^15}      {'Test2':^15}    {'Class. Final':^15}  ")
    print(f'{e.getNome():<8}       {e.getTeste1():<15}      {e.getTeste2():<15}        {e.ClassFinal():<15} \n')

    e.setNome('Carlos')
    e.setTeste1(14)
    e.setTeste2(13)
    print('\n 7_3')
    print(f"{'Nome'}     {'Test1':^15}      {'Test2':^15}    {'Class. Final':^15}  ")
    print(f'{e.getNome():<8}       {e.getTeste1():<15}      {e.getTeste2():<15}        {e.ClassFinal():<15} \n')

    e.setNome = input('Digite o nome correto do aluno(a): ')
    e.setTeste1 = int(input('Digite a nota do Test1 do aluno(a): '))
    e.setTeste2 = int(input('Digite a nota do Test2 do aluno(a): '))

    print('\n 7_4')
    print(f"{'Nome'}     {'Test1':^15}      {'Test2':^15}    {'Class. Final':^15}  ")
    print(f'{e.getNome():<8}       {e.getTeste1():<15}      {e.getTeste2():<15}        {e.ClassFinal():<15} \n')

    print('\n 7_5')

    e.Imprimar()


menu()




from Classe7_7 import *
def main():
    Inf = [["Ana Pinto", 14, 15], ["Rui Pinto", 17, 18],
           ["Carla Silva", 14, 10], ["Telmo Gomes", 10, 12]]
    Pauta = {}
    for a in Inf:
        E = EstudanteInf(a[0], a[1], a[2])
        Pauta[E.Nome] = E.ClassFinal()
    print(Pauta)


main()
'''
from Classe7_7 import *


def SitFinal(CF):
    if CF < 8:
        return "Reprovado"
    elif CF < 10:
        return "Admitido à Oral"
    else:
        return "Aprovado"


def main():
    Inf = [["Ana Pinto", 6, 7], ["Rui Pinto", 17, 18],
           ["Carla Silva", 9, 9], ["Telmo Gomes", 10, 12]]
    Pauta = {}
    for a in Inf:
        E = EstudanteInf(a[0], a[1], a[2])
        Pauta[E.Nome] = (E.ClassFinal(), SitFinal(E.ClassFinal()))
    print(Pauta)


main()
