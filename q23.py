def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    choice = input("Enter '1' to convert from Celsius to Fahrenheit, or '2' to convert from Fahrenheit to Celsius: ")
    
    if choice == '1':
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius} Celsius is equal to {fahrenheit} Fahrenheit")
    elif choice == '2':
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit} Fahrenheit is equal to {celsius} Celsius")
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()