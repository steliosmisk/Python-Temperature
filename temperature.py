import os

print("--WELCOME TO THE TEMPERATURE CONVERTER--")
print("[1] CELSIUS")
print("[2] FAHRENHEIT")
print("[3] KELVIN")
print("[4] RANKINE")
print("[5] EXIT")

while True:
    user_choice = input("Enter your choice: ")
    if user_choice == '5':
        break
    elif user_choice in ['1', '2', '3', '4']:
        os.system('cls')
        try:
            temperature = float(input("Enter the temperature: "))
            if user_choice == '1':
                print(f"Celsius: {temperature}")
                print("Fahrenheit:", temperature * 9/5 + 32)
                print("Kelvin:", temperature + 273.15)
                print("Rankine:", (temperature + 273.15) * 9/5)
            elif user_choice == '2':
                print(f"Fahrenheit: {temperature}")
                print("Celsius:", (temperature - 32) * 5/9)
                print("Kelvin:", (temperature + 459.67) * 5/9)
                print("Rankine:", temperature + 459.67)
            elif user_choice == '3':
                print(f"Kelvin: {temperature}")
                print("Celsius:", temperature - 273.15)
                print("Fahrenheit:", temperature * 9/5 - 459.67)
                print("Rankine:", temperature * 9/5)
            elif user_choice == '4':
                print(f"Rankine: {temperature}")
                print("Celsius:", (temperature - 491.67) * 5/9)
                print("Fahrenheit:", temperature - 459.67)
                print("Kelvin:", temperature * 5/9)
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("Invalid choice. Please enter a number from 1 to 5.")
