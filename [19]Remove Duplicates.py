numbers = list(map(int, input("Enter numbers: ").split()))

result = []

for item in numbers:
    if item not in result:
        result.append(item)

print(result)
