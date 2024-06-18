# sum of the list of numbers
n=int(input("Enter how many numbers do u want to add?"))
lst1=[]
sum=0
for i in range(n):
    num=int(input("Enter the number: "))
    lst1.append(num)
    sum+=num
print("List of numbers:",lst1)
print("Sum of numbers:",sum)
