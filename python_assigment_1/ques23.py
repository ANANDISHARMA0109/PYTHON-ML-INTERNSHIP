# convert celsius to farenheit or vice versa
print("1. Convert farenheit to celsius")
print("2. Convert celsius to farenheit")
ch=int(input("Enter your choice: "))

if ch==1:
    t1=int(input("Enter temperature in Farenheit: "))
    t2=(t1-32)*5/9
    print("Temperature in Celsius:",t2)
elif ch==2:
    t1=int(input("Enter temperature in Celsius: "))
    t2=9/5*t1+32
    print("Temperature in Farenheit:",t2)
else:
    print("Incorrect option")
