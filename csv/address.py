from sys import argv, exit
import csv 

def main():

    # run script with file
    if len(argv) != 2:
        print("Usage: python solution.py file.csv")
        exit(1)

    # open csv and read contents into memory
    with open(argv[1], "r") as file:
        csv_file = csv.DictReader(file)

        # read rows in csv_file
        for row in csv_file:
            if row['Province'] == "Ontario":
                for key, val in row.items():
                    print(key, val)
            

main()