def calculate_sum(numbers):
    return sum(numbers)

def main():
    numbers = input("Enter a list of numbers separated by spaces: ").split()
    numbers = list(map(float, numbers))  # Convert input strings to floats
    sum_numbers = calculate_sum(numbers)
    print("Sum of the numbers:", sum_numbers)

if __name__ == "__main__":
    main()