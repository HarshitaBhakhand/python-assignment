def read_lines_until_empty():
    print("Enter multiple lines of input. Enter an empty line to stop:")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    return lines

def main():
    lines = read_lines_until_empty()
    print("\nLines entered:")
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()