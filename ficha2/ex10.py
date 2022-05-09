
largura = 10
altura = 4
caractere = "#"
print(caractere * largura) # cabeçalho
for i in range(altura):
    espacos = (largura - 2) * ' '
    print("%s%s%s" % (caractere, espacos, caractere)) # meio
print(caractere * largura) # rodapé

#print(largura, altura, caractere)