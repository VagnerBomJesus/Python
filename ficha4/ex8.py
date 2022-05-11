m = 0
n = 0



while m < 1 or m > 999:
    m = int( input("Insert 1 <= m <= 1000:") )
    if  m < 1 or m > 999:
        print("WRONG VALUE! TRY AGAIN!")

while n <= m or n > 1000:
    n = int( input("Insert m < n <= 1000:") )
    if  n <= m or n > 1000:
        print("WRONG VALUE! TRY AGAIN!")

for i in range(m, n+1):
    if i % 2 == 0:    # 500 % 2
        print(i)