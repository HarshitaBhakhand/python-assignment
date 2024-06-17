def check_even_odd():
    num = int(input("Enter a number: "))
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")

if __name__ == "__main__":
    check_even_odd()