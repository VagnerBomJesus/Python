

from classe7_3 import *
from Class7_24 import *
from Class7_26 import *
'''
Bolseiro = {}

Bolseiro[Bolsa("J. Silva")] = [Univ("UP", 2),
                               Brit("BC", "B"), Ginas("Sol", "FdS")]
Bolseiro[Bolsa("A. Gomes")] = [Univ("UCP", 2),
                               Brit("WS", "D"), Ginas("Hol", "18-21")]
Bolseiro[Bolsa("R. Cunha")] = [Univ("UL", 3),
                               Brit("BC", "A"), Ginas("Vir", "14-17")]


for k, v in Bolseiro.items():
    print(
        f"{k.lernome()}\t{v[0].Paga_mensal() + v[1].Paga_mensal() + v[2].Paga_mensal():.0f}€")

'''
'''
y = input('Digite o nome da Equipa: ')
e = Equipa(y)
e.Adicionar()
print('\n')
print(f'Equipa: {y}')
print(f'Nome --- Altura --- Peso')
e.Listar()
'''

'''
def Menu(Titulo, Opcoes, np):

    print(Titulo)
    print()
    for i in range(np):
        print(i + 1, "- ", Opcoes[i])
    print("5 -  Terminar")


def MenuPrincipal():

    print("\n")
    Titulo = "Menu Principal"
    Opcoes = ["Criar",
              "Inseir",
              "Alterar",
              "Suprimir",
              "Alterar",
              ]
    np = 5
    while True:
        op = Menu(Titulo, Opcoes, np)
        if op == 1:
            print("Procedimento Feito")
        elif op == 2:
            print("Procedimento Feito")
        elif op == 3:
            print("Procedimento Feito")
        elif op == 4:
            print("Procedimento Feito")
        else:
            break


MenuPrincipal()
'''


Lista = ["Criar",
         "Inseir",
         "Alterar",
         "Suprimir",
         "Fim"]
while True:

    Opc = Menu(Lista).LerValidar()
    if Opc == len(Lista):
        break
    else:
        ExOp = ExecutarOp(Opc, Lista)
