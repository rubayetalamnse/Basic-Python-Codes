#Write a Python program to convert temperatures to and from celsius, fahrenheit.

temperature = input("Input the  temperature you like to convert? (e.g., 45F, 102C etc.) : ")
degree = int(temperature[0:-1])
temp = temperature[-1]

if temp.upper() == "F":
    celsius_temp = float((degree - 32) * 5/9 )
    print("The temperature -", temperature, "in celsius is", celsius_temp, "degrees.")
elif temp.upper() == "C":
    farenheit_temp = float((9 * degree) / 5 + 32)
    print("The temperature -", temperature, "in celsius is", farenheit_temp, "degrees.")
else:
    print("Input proper temperature.")