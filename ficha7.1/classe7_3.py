from time import sleep


class Menu():
    opcoes = []

    def __init__(self, lista):
        self.opcoes = lista

    def LimparEcran(self):
        print("\n"*50)
        return

    def Afixa(self):
        print("Registo de Disciplinas")
        Num = 1
        for i in self.opcoes:
            print(f"{Num}.{i}")
            Num += 1

    def LerValidar(self):
        while True:
            self.Afixa()
            Num = int(input("Digite 1, 2, 3, 4 ou 5: "))
            if (Num <= 0 or Num > 5):
                print('Opção inválida. Digite um número entre 1 e 5.')
            else:
                return Num


class ExecutarOp():
    def __init__(self, Opc, Lista):

        print(f'Registo de Disciplinas {Lista[Opc - 1]}')
        sleep(2)
        return
