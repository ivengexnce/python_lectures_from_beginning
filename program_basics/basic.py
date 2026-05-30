print("Hello World!")

#Variables are containers for storing data values /Variable stores data + Datatypes
name="Meet"            #data type = String
surname="Maru"
age=19                #Data type = Int - integer  to check data type of var is by using type() func ex.- print(type(age)) output <class 'int'>

residence="Borivali"
weight=70.5           #Data type = Float
is_student=True         #Data type = Boolean ( gives Value of either True or False) used in conditional statements

#method of displaying values of variables 
print(type(age)) #to check data type of var is by using type() func output <class 'int'>
print(name + " " + surname) #concatenation output Meet Maru
print(name,surname) #  Normal/standardized output Meet Maru
print("{} {}".format(name,surname)) #using format method output Meet Maru
print("%s %s"%(name,surname)) #using old style formatting output Meet Maru

#----------------------
print("My name is " + name + " " + surname) #concatenation output My name is Meet Maru
print("My name is", name, surname) # Normal/standardized output My name is Meet Maru
print("My name is {} {}".format(name, surname)) #using format method output My name is Meet Maru


#---- all var in one string using concatenation but in single var combine 
full_name = name + " " + surname + " is " + "resident of " + residence + " having weight of " + str(weight) + " kg" #when useing float data type should use str() func to convert it into string for concatenation otherwise it will give error TypeError: can only concatenate str (not "float") to str
print(full_name) #output Meet Maru is resident of Borivali having weight of 70.5 kg
print(f"my name is {full_name} and i am {age} years old") #using f string output my name is Meet Maru is resident of Borivali having weight of 70.5 kg and i am 19 years old


#---Asking the user for input / taking input from user

#variable=input("Condition/question for user") using without data type will take input as string by default
name=input("what is your name?\t") # \t is used to give tab space after the question
age=input("What is you age? \n") # \n is used to give new line after the question
print(name, age)
print(name +" "+str(age))
print("{}{}".format(name,age))

#variable=datatype(input("Condition/question for user")) to take input in specific data type
weight=float(input("what is your weight (in kg)?\t"))
print(f"Hey my name is {name} and i am {age} yrs old having weight of {weight}kg")

#--now with condition statement for weight is user  entered string instead of no.
if weight and age > 0:
    print(f"hey my name is {name} and i m {age} having weight of {weight} kg")
else:
    print("enter valid inputs")