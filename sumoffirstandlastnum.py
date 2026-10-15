n = int(input("Enter a number: "))

last = n % 10

while n >= 10:
    n //= 10

first = n

sum = first + last

print("Sum of first and last digit:", sum)