def main():
    user_input = input("Enter a string: ")
    with open("output.txt", "w") as file:
        file.write(user_input)
    print("The string has been written to output.txt")

if __name__ == "__main__":
    main()