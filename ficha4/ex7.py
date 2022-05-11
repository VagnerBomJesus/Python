
iNumber = 0
while iNumber < 1 or iNumber > 100:
    iNumber = int( input("Introduza um número entre 1 e 100: ") )
    if iNumber < 1 or iNumber > 100 :
        print("Atenção, o número introduzido não está entre 1 e 100")

for i in range(1, 11):
    print(iNumber, "x ", i, "=", i * iNumber)