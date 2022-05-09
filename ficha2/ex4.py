

categ = str(input('Digite a categoria proficional [A,B,C,D,E,F]: '))
if (categ == 'A') or (categ == 'B') or (categ == 'C'):
    salario = 1500
elif (categ == 'D'):
    salario = 1250 
elif (categ == 'E') or (categ == 'F'):
    salario = 1000 
else:
    salario = 600
print(f'A categoria {salario} € de saláio-base.\n')