import csv

def read_csv_file(filename):
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def main():
    filename = 'data.daa file' 
    read_csv_file(filename)

if __name__ == "__main__":
    main()