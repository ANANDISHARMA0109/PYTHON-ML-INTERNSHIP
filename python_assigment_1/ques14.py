#print multiple lines entered by user
line=input("Enter lines: ")
lst1=[line]
while line!='':
    line=input("Enter lines: ")
    lst1.append(line)
print("Lines entered by the user:")
while lst1!=[] :
    print(lst1.pop(0))
