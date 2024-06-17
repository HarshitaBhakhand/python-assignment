def count_character_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    input_string = input("Enter a string: ")
    frequency = count_character_frequency(input_string)
    print("Character frequency:")
    for char, count in frequency.items():
        print(f"'{char}' : {count}")

if __name__ == "__main__":
    main()