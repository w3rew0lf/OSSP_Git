def inverted(old_dict):
    print("Original dictionary is : ")
    print(old_dict)
    new_dict = dict([(value, key) for key, value in old_dict.items()])
    print("Dictionary after swapping is : ")
    print("keys: values")
    for i in new_dict:
        print(i, " : ", new_dict[i])

old_dict = {'A': 67, 'B': 23, 'C': 45, 'D': 56,
            'E': 12, 'F': 69, 'G': 67, 'H': 23}

inverted(old_dict)


