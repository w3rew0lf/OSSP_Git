
f1 = open("output1.txt", "w")


with open("sample.txt", "r") as myfile:
    data = myfile.read()


data_1 = data[::-1]


f1.write(data_1)

f1.close()
