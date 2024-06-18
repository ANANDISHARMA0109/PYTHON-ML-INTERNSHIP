# generates n numbers of fibonacci series
list1=[0,1]
n=int(input("Enter no of elements in fibonacci series: "))
a=0
b=1
for i in range(n-2):
    sum=list1.append(list1[a]+list1[b])
    a+=1
    b+=1
print("Fibonacci series:",list1)