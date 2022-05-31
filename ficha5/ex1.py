'''
# Ex1
tupla = ()
cat = ["A", "B","C","D"]
n = 100

for i in range(len(cat)):
    nome = input(f"Nome do funcionário {n}: ")
    tupla = tupla + (n, nome, cat[i])
    n += 10
print(tupla)


# Ex2
tupla = (100, "J.Pais", "A", 120, "T. Gomes", "B", 140, "G. Pires", "B", 150, "C.Lima", "C",
         160, "T. Lamas", "B", 170, "H. Gois", "A", 150, "C. Carmo", "D", 180, "T. Lemos", "B")
bc = 0
for i in range(2,len(tupla),3):
    if tupla[i] == "B" or tupla[i] == "C":
        bc+=1
print(f"Há {bc} funcionários das categorias B e C")

# Ex3
tuple_cliente = ()
list_cliente = []
while True:
    nome = input("Digite o nome do Cliente ou ZZZ para terminar: " )
    if nome == 'ZZZ':
        break
    local = input(f"Digite a localidade do {nome}: ")
    tel =  input(f"Digite o telefone do {nome}: ")
    tuple_cliente = (nome, local, tel)
    list_cliente.append(tuple_cliente)
print(list_cliente)
lista_teleC = []
for k in list_cliente:
    nome, local, tel = k
    lista_tele = nome, tel
    lista_teleC.append(lista_tele)
print(lista_teleC)'''


# Ex4
'''compras_cli = (("A. Pinto", "loj_A", "12/02/20",60),
               ("E. Gomes", "Log_B", "10/02/20", 120),
               ("A. Pinto", "loj_A","08/02/20",68),
               ("E. Gomes", "loj_A","07/02/20",75),
               ("A. Pinto", "loj_C","10/02/20",50),
               ("H. Paz", "Luanda", "09/02/20", 24),
               ("A. Pinto", "loj_C", "04/02/20", 26),
               ("A. Pinto", "loj_C", "04/02/20", 24),)

for i in compras_cli:


# EX4
Compras_Cli = (("A. Pinto", "Loj_A", "12/02/20", 60),
    ("E. Gomes", "Loj_B",  "10/02/20", 120),
    ("A. Pinto", "Loj_A","08/02/20", 68),
    ("E.Gomes", "Loj_A", "07/02/20", 75),
    ("A. Pinto", "Loj_C", "10/02/20" , 50),
    ("H. Paz", "Luanda", "09/02/20", 24),
    ("A. Pinto", "Loj_C",  "04/02/20", 26),
    ("A. Pinto", "Loj_C",  "04/02/20", 24))

nome = "A. Pinto"
soma = 0
l_cl = []
Tuplos_PorData = sorted(Compras_Cli, key=lambda x: x[2])
for i in Tuplos_PorData:
    for k in i:
        if k == nome:
            soma += i[3]
            l_cl.append((i[2], soma))
print(f'Totais acumulados por {nome} = {l_cl}')'''

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
'''
pessoas = {'nome': 'vagner', 'sexo':'M','idade':22}

print(pessoas.values())
print(pessoas.keys())
print(pessoas.items())

for k, v in pessoas.items():
    print(f'{k} = {v}')
'''

'''
cafetaria1 = {'Desc': 'Café e bolo de arroz', 'PU': '1.3'}
cafetaria2 = {'Desc': 'Dois cafés e meia torrada', 'PU': '2.2'}
cafetaria3 = {'Desc': 'Meia de leite e tosta com manteiga', 'PU': '3'}
cafetaria4 = {'Desc': 'Galao com tosta mista', 'PU': '3.5'}
menu = list()
menu.append(cafetaria1)
menu.append(cafetaria2)
menu.append(cafetaria3)
menu.append(cafetaria4)
y = 0
tupla = ()
print('{ ', end='')
d = 'Desc='
p = 'PU='

for i in menu:
    y += 1
    print(f'{y}: Menu{  d + i["Desc"] , p + i["PU"]}', end='')
    print(end=', ')
print('}', end='')
'''


'''
cafetaria1 = {'Desc': 'Café e bolo de arroz', 'PU': '1.3'}
cafetaria2 = {'Desc': 'Dois cafés e meia torrada', 'PU': '2.2'}
cafetaria3 = {'Desc': 'Meia de leite e tosta com manteiga', 'PU': '3'}
cafetaria4 = {'Desc': 'Galao com tosta mista', 'PU': '3.5'}
menu = list()
menu.append(cafetaria1)
menu.append(cafetaria2)
menu.append(cafetaria3)
menu.append(cafetaria4)
y = 0
print('=============Menus Disponíveis==============')
for i in menu:
    y += 1
    K = i["PU"]
    D = i["Desc"]
    print("{:>3}. {:<15} {:>10}".format(y, D, K))
'''

cafetaria1 = {'Desc': 'Café e bolo de arroz', 'PU': '1.3'}
cafetaria2 = {'Desc': 'Dois cafés e meia torrada', 'PU': 2.2}
cafetaria3 = {'Desc': 'Meia de leite e tosta com manteiga', 'PU': 3}
cafetaria4 = {'Desc': 'Galao com tosta mista', 'PU': 3.5}
menu = list()
menu.append(cafetaria1)
menu.append(cafetaria2)
menu.append(cafetaria3)
menu.append(cafetaria4)
y = 0

for i in menu:
    y += 1
    K = i["PU"]
    D = i["Desc"]
    print("{:>3}. {:<15} {:>5}".format(y, D, K))

m = float(input("Escolha o menu (1, 2, 3, 4): "))
n = float(input("Quantos menus quer?: "))

if m == 1:
    m = menu[0]
elif m == 2:
    m = menu[1]
elif m == 3:
    m = menu[2]
elif m == 4:
    m = menu[3]

total = m["PU"]*n

print(f'{n:.0f} menus {m["Desc"]} = {total} €')
