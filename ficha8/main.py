

from Classe7_29 import *


def ListaCentrosSeguros(U):
    print(f"{'C. Saúde':10}{'Companhinha de seguro':15}")
    for i in range(len(U)):
        print(f"{U[i].getCSaude():10}{U[i].getComp():14}")


if __name__ == "__main__":
    TU = ((9768123, 1236, "Ramalde", "Medis", 100, 1950, "Ana Pires"),
          (6978111, 2554, "Aldoar", "Ageas", 100, 1970, "Rui Aguiar"),
          (7978223, 3236,  "Paranhos", "Multicare", 120, 1980, "Olga Paiva"),
          (5697831, 2484,  "Bonfim", "Ageas", 190, 1945, "Alda Pais"),
          (1245331, 1297,  "Ramalde", "Medis", 185, 1990, "Pedro Gomes"))
    print(f"{'NUSS':^4}{'NISS':^11}{'C. Saúde':^3}{'Nome':^16}{'A Pagar em €':4}")
    for t in TU:
        U = Utente(t)
        # print(t)
        print(f"{U.SerSaude():14}  {U.getNome():14}{U.Valor():3}")

    U = []
    for i in range(len(TU)):
        U.append(TU[i])
    ListaCentrosSeguros(U)
