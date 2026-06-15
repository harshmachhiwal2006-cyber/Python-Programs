text = input("Enter a string: ")

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for key, value in frequency.items():
    print(f"{key}: {value}")
