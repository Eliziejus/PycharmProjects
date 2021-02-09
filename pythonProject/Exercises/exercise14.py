def new():
    numbers = [1, 2, 5, 4, 7, 22, 3, 6, 2, 7, 1, 6, 1]
    b = []

    numbers = list(dict.fromkeys(numbers))
    b.append(numbers)
    return b

print(new())

