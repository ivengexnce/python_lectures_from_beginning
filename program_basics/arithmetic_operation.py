#basic operations without library
#variables /data
name="Meet"            #data type = String
surname="Maru"
age=19                #Data type = Int - integer  to check data type of var is by using type() func ex.- print(type(age)) output <class 'int'>
a=float(input("Enter the value :"))
b=float(input("Enter the value :"))

#operation 1 sum=a+b
#operation 2 divide=a/b
#operation 3 multiply=a*b

choice=input("Enter the operation you want to perform (sum/divide/multiply):")
if choice=="sum" or choice=="1":
    print(a+b);
elif choice=="divide" or choice=="2":
    if b!=0:
        print(a/b);
    else:
        print("Error: Division by zero is not allowed.")
        
elif choice=="multiply" or choice=="3":
    print(a*b);
else:
    print("Invalid choice! Please enter sum, divide, or multiply.")
