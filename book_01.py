"""
Referência:
Python Programming Exercises, Gently Explained (Al Sweigart) - p.130
"""

def bubbleSort(numbers):
    for i in range(len(numbers) -1): # i começa e termina 1 index antes de j
        for j in range(i, len(numbers)):
            if numbers[i] > numbers [j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers

assert bubbleSort([2, 0, 4, 1, 3]) == [0, 1, 2, 3, 4]
assert bubbleSort([2, 2, 2, 2]) == [2, 2, 2, 2]
print(bubbleSort([2, 0, 4, 1, 3]))