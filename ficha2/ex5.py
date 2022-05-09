
produto = str(input('Três primeiras letras da classe do produto?: '))

if(produto =='VEG'):
    desconto = 0.15*100
elif (produto =='LAC'):
    desconto = 0.10*100
elif (produto =='RES'):
    desconto = 0.01 * 100

print (f'Os produtos da classe {produto} têm {desconto:.0f}% de desconto.')    
