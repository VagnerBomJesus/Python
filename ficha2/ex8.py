myList =[] 
salario =[]
names = []
total = totalFuture = 0
while True:
    new_nome = input("Digite o nome do funcionário? (ZZZ para terminar): " )
    if new_nome.upper() == 'ZZZ':
        break
    new_salario =  float(input(f"Digite o salário atual do funcionário {new_nome}?: ")) 
    names.append(new_nome)
    salario.append(new_salario)

print(f'Nome       Sal.Atual      Sal.Futuro')   
for i in range(len(salario)):  
    if salario[i] == 0 and salario[i] <= 500:
        myList.append(salario[i] + salario[i]*0.10)       
    elif salario[i] >= 501 and salario[i] <= 800:
         myList.append(salario[i] + salario[i]*0.05)     
    else:
         myList.append(salario[i])

    total = total + salario[i]
    totalFuture = totalFuture + myList[i]

    print(f'{names[i]}      {salario[i]:.2f}        {myList[i]:.2f}')
        
print(f'Massa sal. Atual = {total:.2f}')
print(f'Massa sal. Futuro = {totalFuture:.2f}')
       
 