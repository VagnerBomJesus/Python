jogadores = ["Ana", "Rui", "Telmo", "Beatriz", "Luisa", "Joana", "Manuel", "Pedro", "Paulo", "Paulino", "Maria", "Tereza", "Pedro", "Ricardo"]
lista = []
k = v = 0

for i in range(0,len(jogadores),2):
    v+= 1
    print(f"Equipa {v} = ['{jogadores[i]}', '{jogadores[i+1]}']")