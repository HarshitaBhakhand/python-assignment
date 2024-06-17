def concatenate_strings():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    concatenated_string = str1 + str2
    return concatenated_string

def main():
    result = concatenate_strings()
    print("Concatenated string:", result)

if __name__ == "__main__":
    main()