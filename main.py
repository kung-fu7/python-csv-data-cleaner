import csv


def main():
    print("CSV Data Cleaner Started")

    file_path = "data/customers.csv"

    with open(file_path, "r", newline="") as file:
        reader = csv.reader(file)

        headers = next(reader)
        records = list(reader)

    print("\nCustomer Records:")

    for record in records:
        print(" | ".join(record))

    print("\nTotal records:", len(records))

    print("\nColumns:")
    print(", ".join(headers))


if __name__ == "__main__":
    main()
