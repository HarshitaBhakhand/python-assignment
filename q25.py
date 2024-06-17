def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src, open(destination_file, 'w') as dest:
            dest.write(src.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")
    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()