def list_sum(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sum:", list_sum(numbers))
