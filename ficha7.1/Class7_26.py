class Jogador:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def imprime(self):
        return self.nome + "---"+str(self.altura) + "cm ---"+str(self.peso)+"kg"


class Equipa:
    Efetivos = []

    def __init__(self, n):
        self.nome = n

    def Adicionar(self):
        nome = input("Nome do jogador ou ZZZ: ")
        while nome.lower() != "zzz":
            a = int(input("Altura em cm: "))
            p = int(input("Peso em Kg: "))
            J = Jogador(nome, a, p)
            self.Efetivos.append(J)
            nome = input("Nome do jogador ou ZZZ: ")

    def Listar(self):
        for J in self.Efetivos:
            print(J.imprime())
