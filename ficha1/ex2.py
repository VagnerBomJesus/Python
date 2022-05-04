
# Recebendo a entrada do usuário
print("\n")
d1 = float(input("Introduza a despesa do 1º dia: "))
d2 = d1 + (d1*0.2)
d3 = d2 + (d2*0.2)
d4 = d3 + (d3*0.2)

med = (d1+d2+d3+d4)/4

print(f'Despesa média diária {med:4.2f} euros')