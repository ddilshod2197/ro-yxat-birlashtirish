def bubble_sort():
    numbers = []
    for i in range(5):
        son = int(input(f"Sizni {i+1}-soni kiriting: "))
        numbers.append(son)

    for i in range(len(numbers)):
        for j in range(len(numbers) - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

    print("Saralangan sonlar: ", numbers)

bubble_sort()
