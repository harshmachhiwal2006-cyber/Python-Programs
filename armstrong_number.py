# armstrong_number.py
# Program to check whether a number is an Armstrong number

num = int(input("Enter a number: "))

total = 0
temp = num
digits = len(str(num))

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == num:
    print(f"{num} is an Armstrong Number")
else:
    print(f"{num} is not an Armstrong Number")
