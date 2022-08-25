import sys
def revfile(x):
    i=0
    z=len(open(x).readlines())
    rev=[None]*z
    f=open(x)
    while(i<z):
         rev[i]=f.readline()
         i=i+1
    while(i>0):
        i=i-1
        rev[i]=rev[i].strip()
        print(rev[i])
z="a.txt"
revfile(z)
