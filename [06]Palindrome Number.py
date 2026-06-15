num = int(input("Enter a number: "))

original = str(num)

if original == original[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
