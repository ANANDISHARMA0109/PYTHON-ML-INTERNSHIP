#occurences of specific element in list
lst=[]
n=int(input("Enter no of elements of list: "))
for i in range(n):
    val=input("Enter element: ")
    lst.append(val)
ele=input("Enter the element whose occurence  is to be find: ")
count=0
for i in range(n):
    if lst[i]==ele:
        count+=1
print("Frequency of the given element:",count)