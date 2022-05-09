nome = []
ingles = []
estagio = []
internacional = []
while True:
    new_nome = input("Nome do canidato? (ZZZ para terminar): " )
    if new_nome.upper() == 'ZZZ':
        break
    new_estagio = int(input("Nota de estágio?: "))
    new_internacional = input("Carreira interbncional?: ")
    new_ingles = input("Fluente em Inglês?: ")
    nome.append(new_nome)
    estagio.append(new_estagio)
    internacional.append(new_internacional)
    ingles.append(new_ingles)

print('Nome        Observação')  
for i in range(len(nome)):  
    if new_estagio > 12 and new_internacional == 'S' and new_internacional == 'S' and new_ingles == 'S' :
        print(f'{nome[i]}       Selecionado(a)')
    else:
        print(f'{nome[i]}       Eliminada(a)')


