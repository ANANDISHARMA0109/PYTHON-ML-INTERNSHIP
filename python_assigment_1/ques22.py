# min and max value in a list of numbers
n=int(input("Enter the no of elements of list: "))
lst=[]
for i in range(n):
    num=int(input("Enter the numbers: "))
    lst.append(num)
print("List of numbers:",lst)
lst.sort()
print("minimum value:",lst[0])
print("maximum value:",lst[-1])