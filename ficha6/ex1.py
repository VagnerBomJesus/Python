
# Exerc.2
# Maior e menor de três numeros: Complete o seguinte programa,
# definindo duas funções que calculem o maior e o menor de três numeros inteiros.
#
# Construa as Funções:
'''
def MaiorDe3(X, Y, Z):
    max = X
    if Y > max:
        max = Y
    if Z > max:
        max = Z
    return max


def MenorDe3(X, Y, Z):
    min = X
    if Y < min:
        min = Y
    if Z < min:
        min = Z
    return min


def menu():
    X = int(input("Digite o primeiro valor (X): "))
    Y = int(input("Digite o segundo valor (Y): "))
    Z = int(input("Digite o terceiro valor (Z): "))
    print(f"Maior= {MaiorDe3(X, Y, Z)}")
    print(f"Menor= {MenorDe3(X, Y, Z)}")


menu()

'''
'''
# Exerc.3
# Horas minutos e segundos: Elabore funções que
# convertam um determinado número de segundos em horas, minutos e segundos
# Construa as funções


def Calc_Hor(Seg):
    return (Seg/3600) % 60


def Calc_Seg(Seg):
    return (Seg) % 60


def Calc_Min(Seg):
    return (Seg/60) % 60


# Programa principal
def menu():
    Seg = int(input("Digite o número de segundos a converter: "))
    S = Calc_Seg(Seg)
    M = Calc_Min(Seg)
    H = Calc_Hor(Seg)
    print(f"{Seg} segundos = {H:02.0f}:{M:02.0f}:{S:02.0f}")


menu()
# Output
# Digite o número de segundos a converter 3764
# 3764 segundos=01:02:44

'''

# Exerc.4
# Elabore a função EscritaCidades que lista as cidades
# cujos nomes começam pelas letras C,D,E,F ou G. A Função
# EscritaCidades é invocada pelo seguinte programa:

'''
def LeituraCidades(A):
    for I in range(len(A)):
        A[I] = input(f"Cidade {I+1}=")
    return A
def EscritaCidades(A):
    # complete a função
    for I in A:
        if I[0].upper() >= "C" and I[0].upper() < "H":
            print(I)
    return
def menu():
    N = int(input("Quantas cidades há?: "))
    A = [""]*N
    print(A)
    LeituraCidades(A)
    EscritaCidades(A)
menu()
'''
# Exerc.5
# Elabore a função Contagem que conta o número de vezes que cada elemento ocorre
# numa lista e completa o seguinte programa:

# 1. pressupor que cada elemento da lista ocorre uma vez
# 2. Comparar cada elemento da lista com os seguintes
#    2.1Enquanto houver elementos, e o elemento for igual ao elemento seguinte,
#     incrementar o contador do elemento e colocar a zero o contador do elemento seguinte
# ........................................................................................
# Output
# Quantos elementos tem a lista?6
# A[1]=1
# A[2]=2
# A[3]=3
# A[4]=4
# A[5]=5
# A[6]=6
# 1.0 ocorre 1 vez(es) na lista
# 2.0 ocorre 1 vez(es) na lista
# 3.0 ocorre 1 vez(es) na lista
# 4.0 ocorre 1 vez(es) na lista
# 5.0 ocorre 1 vez(es) na lista
# 6.0 ocorre 1 vez(es) na lista
'''

def Leitura(A):
    for I in range(len(A)):
        A[I] = float(input(f"A[{I+1}]="))
    A.sort(reverse=False)
    return A


def Escrita(A, Conta):
    for I in range(len(A)):
        if Conta[I] != 0:
            print(f"{int(A[I])} ocorre {Conta[I]} vez(es) na lista")
    return


def Contagem(A):
   # elabore a função
    C = [1]*len(A)
    for I in range(len(A)-1):
        if C[I] != 0:
            J = I+1
            while J < len(A) and A[I] == A[J]:
                C[I] += 1
                C[J] = 0
                J += 1
    return C


def menu():
    N = int(input("Quantos elementos tem a lista?: "))
    A = [0]*N
    Leitura(A)
    Conta = Contagem(A)
    Escrita(A, Conta)


menu()



import numpy as np
def LeituraRespostas(Resp):
    for A in range(0, Resp.shape[0]):
        for J in range(0, Resp.shape[1]):
            Resp[A][J] = input(f"Resposta do aluno {A+1} à perg. {J+1} ")

def ClassifTotais(Chave, Cotacao, Resp):
    print(f"\n Aluno Classificação")
    for A in range(0, Resp.shape[0]):
        final = (Resp[A] == Chave)*Cotacao
        print(f"{A+1:^5}{final.sum():^15}")

def menu():
    Chave = np.array(['a', 'b', 'c', 'c', 'd', 'a'])
    Cotacao = np.array([1, 2, 3, 3, 2, 2])
    N = int(input("Quantos alunos há? "))
    M = Chave.shape[0]
    Resp = np.empty((N, M), dtype=str)
    LeituraRespostas(Resp)
    ClassifTotais(Chave, Cotacao, Resp)

menu()
'''
# Exerc.6
# Elabore um programa que imprima, o Triangulo de pascal é formado
# por números que apresentam diversas relações entre eles. O triangulo pode inscrever-se numa
# matriz em que o topo ocupa a posição central da primeira linha da matriz.
# Cada um dos restantes números é a soma dos números que estão na linha imediatamente acima
# à sua esquerda e à sua direita. Os lados do triangulo são formados pela unidade.

# Output

# Altura do triângulo? 8

#                         1
#                     1     1
#                    1     2     1
#                 1     3     3     1
#             1     4     6     4     1
#           1     5    10    10     5     1
#        1     6    15    20    15     6     1
#    1     7    21    35    35    21     7     1

# resolução
# T - Matriz onde se escreve o triangulo de pascal,
# N - altura do Triangulo,
# Meio - Indice do meio da matriz onde se inscreve o triangulo)

'''
def Triangulo(T, N):
   # elabore a função
    T[0][N] = 1
    for I in range(1, N):
        for J in range(N-I, N+I+1, 2):
            T[I][J] = T[I-1][J-1]+T[I-1][J+1]
    return


def ImpressaoTriangulo(T, N):
    # elabora a função
    for I in range(0):
        print()
        for J in range(0, N*2+1):
            if T[I][J] == 0:
                print("{0:3}".format(""), end="")
            else:
                print("{0:3d}".format(T[I][J]), end="")
    return

# programa principal


def menu():
    N = int(input("Altura do triângulo? "))
    T = [[0]*(2*N+1) for i in range(N)]

    Triangulo(T, N)
    ImpressaoTriangulo(T, N)


menu()
'''

# Exer7.1

# Relativamente ao exer6, saiba que temos dois módulos: Leitura.py que
# contém a função LeituraRespostas e Classificacoes.py que contém a função Classiftotais.

# Altere o programa principal de modo a
# invocar as funções dos módulos Leitura e Classificações


'''
def menu():
    Chave = np.array(['a', 'b', 'c', 'c', 'd', 'a'])
    Cotacao = np.array([1, 2, 3, 3, 2, 2])
    N = int(input("Quantos alunos há? "))
    M = Chave.shape[0]
    Resp = np.empty((N, M), dtype=str)
    Leitura.LeituraRespostas(Resp)
    Classificacoes.ClassifTotais(Chave, Cotacao, Resp)


menu()'''


'''

def LeituraRespostas(Resp):
    for A in range(0, Resp.shape[0]):
        for J in range(0, Resp.shape[1]):
            Resp[A][J] = input(f"Resposta do aluno {A+1} à perg. {J+1} ")


def ClassifTotais(Chave, Cotacao, Resp):
    print(f"\n Aluno Classificação")
    for A in range(0, Resp.shape[0]):
        final = (Resp[A] == Chave)*Cotacao
        print(Resp[A] == Chave)
        print(f"{A+1:^5}{final.sum():^15}")


'''




from ficha6.Classificacoes import  ClassifTotais
from ficha6.Leitura import LeituraRespostas
def menu():
    Chave = np.array(['a', 'b', 'c', 'c', 'd', 'a'])
    Cotacao = np.array([1, 2, 3, 3, 2, 2])
    N = int(input("Quantos alunos há? "))
    M = Chave.shape[0]
    Resp = np.empty((N, M), dtype=str)

    LeituraRespostas(Resp)
    ClassifTotais(Chave, Cotacao, Resp)


menu()


'''
from ficha6.Classificacoes import ClassifTotais
from ficha6.Leitura import LeituraRespostas
import numpy as np
def main():
    res = np.array(['a', 'b', 'c'])
    valor = np.array([5, 5, 10])
    num_aluno = int(input("Numero de aluno? ->"))
    Resp = np.empty((num_aluno, len(res)), dtype=str)
    LeituraRespostas(Resp)
    ClassifTotais(res, valor, Resp)

main()
'''
