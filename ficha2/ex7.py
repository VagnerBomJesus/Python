cInicial = float(input('Capital inicial?: '))

meta = cInicial * 1.2
taxa=2.5
aculado = 0
anos = 0
while aculado < meta:
    anos+=1
    aculado = cInicial * (1+taxa/100)**anos

print(f'{aculado:.2f}€ ao fim de {anos} anos')