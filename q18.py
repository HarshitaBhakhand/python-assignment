def are_anagrams(string1, string2):
    return sorted(string1.lower()) == sorted(string2.lower())

def main():
    string1 = input("Enter the first string: ")
    string2 = input("Enter the second string: ")
    if are_anagrams(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams.")
    else:
        print(f"'{string1}' and '{string2}' are not anagrams.")

if __name__ == "__main__":
    main()