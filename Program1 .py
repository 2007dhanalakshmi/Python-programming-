
# Fahrenheit to Celsius and Celsius to Fahrenheit Conversion

ch = int(input("Enter Your Choice either 1 or 2: "))

if ch == 1:
    F = int(input("Enter a temperature in Fahrenheit: "))
    C = (F - 32) * 5.0 / 9.0
    print("Temperature:", F, "Fahrenheit =", C, "C")

elif ch == 2:
    Cel = int(input("Enter a temperature in Celsius: "))
    Fa = 9.0 / 5.0 * Cel + 32
    print("Temperature:", Cel, "Celsius =", Fa, "F")

else:
    print("Invalid choice")
  
output:
enter your choice either 1 or 2:1
enter a temperature in fahrenheit:100
temperature:100 fahrenheit=37.77778c
enter your choice either 1 or 2:2
enter a temperature in celsius:35
temperature:35celsius=95.0F
