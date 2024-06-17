def find_min_max(input_list):
    min_value = min(input_list)
    max_value = max(input_list)
    return min_value, max_value

def main():
    input_list = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))
    min_value, max_value = find_min_max(input_list)
    print(f"The minimum value in the list is {min_value}")
    print(f"The maximum value in the list is {max_value}")

if __name__ == "__main__":
    main()