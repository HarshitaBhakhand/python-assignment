import string

def remove_punctuation(input_string):
    return input_string.translate(str.maketrans('', '', string.punctuation))

def main():
    input_string = input("Enter a string with punctuation: ")
    cleaned_string = remove_punctuation(input_string)
    print("String without punctuation:", cleaned_string)

if __name__ == "__main__":
    main()