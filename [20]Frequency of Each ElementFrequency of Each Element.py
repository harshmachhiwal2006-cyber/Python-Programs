numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for item in numbers:
    frequency[item] = frequency.get(item, 0) + 1

print(frequency)
