def group(l, size):
    return [l[i:i+size] for i in range(0, len(l), size)]
print(group([1, 2, 3, 4, 5, 6, 7, 8, 9], 2))
