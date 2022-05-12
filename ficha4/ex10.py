

jogadoresP = ["Ana", "Rui", "Telmo", "Beatriz", "Luisa", "Joana", "Manuel"]
jogadoresL = ["Pedro", "Paulo", "Paulino", "Maria", "Tereza", "Pedro", "Ricardo"]
v = 0
if(len(jogadoresL) != len(jogadoresP)):
    if(len(jogadoresL) > len(jogadoresP)):
        jogadoresP.append("Vagner")
    else:
        jogadoresL.append("Vagner")

totalEquipa = jogadoresP.copy() + jogadoresL.copy()
print(f'Jogadores Para o Torneio: {totalEquipa}')
for i in range(0,len(jogadoresL),2):
    v+= 1
    print(f"Equipa {v} = ['{jogadoresL[i]}', '{jogadoresP[i]}']")

