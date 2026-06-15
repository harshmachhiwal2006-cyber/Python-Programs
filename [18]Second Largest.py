numbers = list(map(int, input("Enter numbers separated by space: ").split()))

unique = list(set(numbers))
unique.sort()

print("Second largest:", unique[-2])
