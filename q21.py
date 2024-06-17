def count_occurrences(input_list, element):
    return input_list.count(element)

def main():
    input_list = input("Enter a list of elements separated by spaces: ").split()
    element = input("Enter the element to count: ")
    occurrences = count_occurrences(input_list, element)
    print(f"The element '{element}' appears {occurrences} times in the list.")

if __name__ == "__main__":
    main()