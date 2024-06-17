def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

def main():
    number = int(input("Enter a number: "))
    sum_digits_result = sum_of_digits(number)
    print(f"The sum of the digits of {number} is {sum_digits_result}")

if __name__ == "__main__":
    main()