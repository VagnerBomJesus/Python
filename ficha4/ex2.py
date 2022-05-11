'''
i = -12
while i <= -6:
    print(i, end=" ")
    i = i + 1


n = -1
while n < 0 or n > 20:
    n = int(input("Insert positive integer number: "))
    if n < 0 or n > 20:
        print("Please notice the interval for the number.")

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(n, "! = ", end="", sep="")
for i in range(n, 1, -1):
    print(i, "x", end="", sep="")

print("1 = ", factorial, sep="")
'''
