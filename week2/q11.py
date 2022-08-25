def check_even(x):
    if(x%2==0):
         return False
    else:
         return True
numbers = [1,2,3,4,5]
even_numbers = filter(check_even,numbers)
print(list(even_numbers))
