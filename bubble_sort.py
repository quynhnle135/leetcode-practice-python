def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if (numbers[j] > numbers[j + 1]):
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers

arr = [1, 7, 4, 3, 5, 2, 8]
print(bubble_sort(arr))