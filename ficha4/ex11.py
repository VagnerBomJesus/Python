'''
Elabora um programa que divida a seguinte lista de jodadores em equi de três jogadores
'''

jogadore = ["Ana", "Rui", "Telmo",  "Manuel", "Pedro", "Paulo", "Paulino", "Maria", "Tereza", "Pedro", "Ricardo", "Vagner"]
k = 0
for i in range(0,len(jogadore),3):
    k+=1
    print(f"Equipa {k} = ['{jogadore[i]}', '{jogadore[i+1]}', '{jogadore[i+2]}']")