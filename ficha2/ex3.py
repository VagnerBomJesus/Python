

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))

if (a>b) and (a>c) and (b>c):
    print(f'{a} é o maior de {b}, {c} e {c}')
elif (b>a) and (b>c) and (a>c):
    print(f'{b} é o maior de {a}, {c} e {c}')
elif (c>a) and (c>b) and (a>b):
    print(f'{c} é o maior de {a}, {b} e {c}')


