# 3. Implemente um programa que imprima todos os números inteiros múltiplos de 3 entre 5 e 1000 (inclusive), um por linha, com saltos de 3. Algo semelhante a:

i = 6
while i < 1001 :
    print( i )
    i = i + 3


for i in range(5,1001):
    if i%3 == 0:
      print( i )