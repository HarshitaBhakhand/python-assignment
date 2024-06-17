def main():
    try:
        with open("output.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist.")

if __name__ == "__main__":
    main()
