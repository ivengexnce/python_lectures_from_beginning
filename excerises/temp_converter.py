#===Temperature-Converter===

#taking the input from user in Celsius
celsius=float(input("Enter the Temperature in Celsius: "))

#converting the celsius to fahrenheit
fahrenheit=(celsius*9/5)+32

print(f"The Temperature in Fahrenheit is : {fahrenheit:.2f}")

if celsius < 0:
    print("its Freezing!!")
elif celsius < 15:
    print("its Cold!!")
elif  celsius < 25:
    print("its Pleasant!!")
elif 25 <= celsius < 35:
    print("its Warm!!")
else:
    print("its hot!!")

