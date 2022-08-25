def find_duplicates(list_of_numbers):
    #start writing your code here
    x=set(list_of_numbers)
    y=[]
    dup=[]
    count=0
    for i in x:
        y.append(i)
    for i in y:
        for j in list_of_numbers:
            if(j==i):
                count+=1
            if count>=2:
                    dup.append(i)
                    break
        count=0
    return dup

list_of_numbers=[1,2,3,4,1,5,2,6,2,6,3,6,7,1,4,2]
list_of_duplicates=find_duplicates(list_of_numbers)
print(list_of_duplicates)
