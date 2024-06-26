def check_prefix_suffix(input_string, prefix, suffix):
    starts_with_prefix = input_string.startswith(prefix)
    ends_with_suffix = input_string.endswith(suffix)
    return starts_with_prefix, ends_with_suffix

def main():
    input_string = input("Enter a string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")
    starts_with_prefix, ends_with_suffix = check_prefix_suffix(input_string, prefix, suffix)
    
    if starts_with_prefix:
        print(f"The string '{input_string}' starts with '{prefix}'.")
    else:
        print(f"The string '{input_string}' does not start with '{prefix}'.")
        
    if ends_with_suffix:
        print(f"The string '{input_string}' ends with '{suffix}'.")
    else:
        print(f"The string '{input_string}' does not end with '{suffix}'.")

if __name__ == "__main__":
    main()