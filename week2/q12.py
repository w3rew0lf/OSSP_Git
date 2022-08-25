def finding_middle(n):

    if(n%2==0):
        return ((n)//2)
    else:
        return ((n+1)//2)


def write_triplets(n):
    to_return = []

    if len(n) >= 2:
        for i in n:
            for j in range(1, finding_middle(i)):
                triplet = (j, i-j, i)
                to_return.append(triplet)

    return to_return

print("Enter the values:")
val =  [int(x) for x in input().strip().split(' ')]
out = write_triplets(val)
print(out)
