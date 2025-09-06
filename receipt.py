import csv
from datetime import datetime

def main():
    PRODUCT_NUM = 0
    items = 0
    subtotal = 0
    sales_tax_rate = 0.06

    try:
        products_dict = read_dictionary("products.csv", PRODUCT_NUM)

        print("Bryce Emporium\n")

        current_date_and_time = datetime.now()

        with open ("request.csv", "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for row in reader:
                value = row[PRODUCT_NUM] 
                quantity = int(row[1])
                product_info = products_dict[value]
                product_name = product_info[1]
                product_price = float(product_info[2])
                items += quantity
                subtotal += quantity * product_price

                print(f"{product_name}: {quantity} @ {product_price}")

    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file\n{key_err}")
    
    except FileNotFoundError as not_found_err:
        print(f"Error: missing file\n{not_found_err}")
    
    rounded_subtotal = round(subtotal, 2)
    sales_tax = rounded_subtotal * sales_tax_rate
    rounded_sales_tax = round(sales_tax, 2)
    total = rounded_subtotal + rounded_sales_tax
    
    print(f"\nNumber of Items: {items} ")
    print(f"Subtotal: {rounded_subtotal} ")
    print(f"Sales Tax: {rounded_sales_tax} ")
    print(f"Total: {total} \n")
    print("Thank you for shopping at the Bryce Emporium.")
    print(f"{current_date_and_time:%a %b %d %H:%M:%S %Y}\n")

    print("We would love to hear your feedback! Please complete our online survey at:")
    print("www.bryceemporium.com/survey\n")


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    compound_dict = {}

    try:
        with open(filename, "rt") as csv_file:
            reader = csv.reader(csv_file)
            next(reader)

            for product in reader:
                key = product[key_column_index]
                compound_dict[key] = product

    except FileNotFoundError as not_found_err:
        print(f"Error: missing file\n{not_found_err}")

    except KeyError as key_err:
        print(f"Error: unknown product ID in the request.csv file\n{key_err}")

    return compound_dict

if __name__ == "__main__":
    main()
