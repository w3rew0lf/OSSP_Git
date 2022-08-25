import sys
f2 = open("output2.txt", "w")
with open("sample.txt", "r") as myfile:
    data = myfile.readlines()

data_2 = data[::-1]

f2.writelines(data_2)

f2.close()
