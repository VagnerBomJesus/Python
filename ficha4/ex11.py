'''
Elabora um programa que divida a seguinte lista de jodadores em equi de três jogadores
'''

jogadores = ["Ana", "Rui", "Telmo", "Beatriz", "Luisa", "Joana", "Manuel", "Pedro", "Paulo", "Paulino", "Maria", "Tereza", "Pedro", "Ricardo"]
jogadore = ["Ana", "Rui", "Telmo",  "Manuel", "Pedro", "Paulo", "Paulino", "Maria", "Tereza", "Pedro", "Ricardo", "Vagner"]
lista = []
k = v = 0

for i in range(0,len(jogadores),2):
    v+= 1
    print(f"Equipa {v} = ['{jogadores[i]}', '{jogadores[i+1]}']")

print('\n')

for i in range(0,len(jogadore),3):
    k+=1
    print(f"Equipa {k} = ['{jogadore[i]}', '{jogadore[i+1]}', '{jogadore[i+2]}']")