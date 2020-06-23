import array as arr
array=list()
number=input("enter the number of elements you want:")
for i in range(int(number)):
    n=input("number:")
    array.append(n)
    print("ARRAY:",array)
print(sorted(array))
sarray=sorted(array)
print(sarray.pop(-2))
