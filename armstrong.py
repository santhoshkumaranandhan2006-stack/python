n = int(input("Enter a number: "))

temp = n
total = 0
digits = len(str(n))

while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

