list1 = []
num= int(input("Enter the number of elements in the list: "))
for i in range(0, num):
    element= int(input("Enter the element: "))
    list1.append(element)
print(list1)
list2 = []
for j in list1:
    if j > 0:
        list2.append(j)
print(list2)