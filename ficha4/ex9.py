n = -1
while n < 0 or n > 20:
    n = int(input("Insert positive integer number: "))
    if n < 0 or n > 20:
        print("Please notice the interval for the number.")

factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print(n, "! = ",factorial, end="", sep="")


