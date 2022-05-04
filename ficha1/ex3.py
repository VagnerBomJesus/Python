

nome = str(input("Digite o nome do Vendedor: "))
sBase = float(input("Digite o salário base: "))
cPorCarro = int(input("Comissão por cada carro vendido: "))
p = float(input("Digite a percentagem sobre o valor das ventas (%): "))


nCarros = int(input("Número de carros vendido: "))
vVenda = float(input("Digite o valor das ventas: "))

c_Comicao = cPorCarro * nCarros

v_Venda = (vVenda * p)/100

sFinal = sBase + round(c_Comicao, 2) + v_Venda

print(f'Salário a processar para {nome} {sFinal:4.2f} euros')
