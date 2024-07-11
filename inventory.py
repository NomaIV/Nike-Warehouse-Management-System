from tabulate import tabulate
import sys

# Class definition for Shoe
class Shoe:
    def __init__(self, country, code, product, cost, quantity):
        # Initialize the attributes, casting cost and quantity to integers
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)  # Cast cost to an integer
        self.quantity = int(quantity)  # Cast quantity to an integer

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return(f"Country: {self.country}, Code: {self.code}, Product: {self.product}, Cost: {self.cost}, Quantity: {self.quantity}")

# List to store Shoe objects
shoe_list = []

# Function to read data from the 'inventory.txt' file
def read_shoes_data():
    try:
        with open("inventory.txt", "r") as file:
            next(file)  # Skip the header
            for line in file:
                try:
                    data = line.strip().split(",")
                    # Convert cost and quantity to integers
                    shoes_object = Shoe(data[0], data[1], data[2], data[3], data[4])
                    shoe_list.append(shoes_object)
                except Exception as e:
                    print(f"Error creating shoes object: {e}")

    except FileNotFoundError:
        print("File 'inventory.txt' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to capture new shoes
def capture_shoes():
    while True:
        try:
            country = input("Please enter country: ")
            code = input("Please enter code: ")
            product = input("Please enter product: ")
            cost = int(input("Please enter cost: "))
            quantity = int(input("Please enter quantity: "))

            new_shoe = Shoe(country, code, product, cost, quantity)
            shoe_list.append(new_shoe)

            # Append the new shoe data to the text file
            with open("inventory.txt", "a") as file:
                file.write(f"{country},{code},{product},{cost},{quantity}\n")

            print("New shoe captured successfully!")
            break  # Exit the loop if the input is valid

        except ValueError:
            print("Invalid input. Please enter a valid number for cost and quantity.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Function to view all shoes
def view_all():
    try:
        # Check if shoe list is empty
        if not shoe_list:
            print ("No shoes to display. ")
            return
        
        # Create a list of lists for tabulate 
        table_data = [[shoe.country, shoe.code,shoe.product, shoe.cost, shoe.quantity ] for shoe in shoe_list]

        # Define headers for the table
        headers = ["Country", "Code", "Product", "Cost", "Quantity"]

        # Print table using tabulate 
        print(tabulate(table_data, headers=headers, tablefmt="grid"))

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to re stock shoes
def re_stock():
    try:
        # Find shoe object with the lowest quantity
        min_quantity_shoe = min(shoe_list, key=lambda x:x.quantity)

        # Print details of shoe object with the lowest quantity
        print(f"\nLowest quantity shoe details: \n{min_quantity_shoe}\n ")

        # Ask user if they want to restock
        restock_choice = input("Do you want to restock? (yes/no): ").lower()

        if restock_choice =="yes":

        # Get quantity to restock
            restock_quantity = int(input(f"Please enter quantity to restock for {min_quantity_shoe.product }:"))

        # Update quantity in Shoe object
            min_quantity_shoe.quantity += int(restock_quantity)

        # Update inventory.txt file with new quantity
            with open("inventory.txt", "r") as file:
                lines = file.readlines()

        # Update quantity in appropriate lines
            for i, line in enumerate(lines):
                if min_quantity_shoe.code in line:
                    lines[i] = f"{min_quantity_shoe.country}, {min_quantity_shoe.code}, {min_quantity_shoe.product}, {min_quantity_shoe.cost}, {min_quantity_shoe.quantity}\n"

        # Write modified lines in inventory.txt file
            with open("inventory.txt", "w") as file:
                file.writelines(lines)

                print(f"\nRestock successful! Update quantity: {min_quantity_shoe.quantity}\n")   

        elif restock_choice == "no":
            print("\nNo restock performed.\n")

        else:
            print("\nInvalid choice. Please enter 'yes' or 'no'. \n")

    except ValueError:
        print("Invalid input. Please enter a valid number for restock quantity. ")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    

# Function to search shoes
def search_shoe():
    try:
        code_to_search = input("Please enter code of the shoe to search: ")

        # Search for shoe in list
        found_shoe = next((shoe for shoe in shoe_list if shoe.code == code_to_search), None)

        if found_shoe:
            print(f"Shoe found: {found_shoe}\n")

        else:
            print("Shoe not found.\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function of value per item
def value_per_item():
    try:
        # Check if shoe list is empty
        if not shoe_list:
            print("No shoes to calculate value. ")
            return
        
        # Print headers
        print("\nTotal Value for each item: ")
        print(".............................")

        # Calculate and print total value for each item
        for shoe in shoe_list:
            total_value = shoe.cost * shoe.quantity
            print(f"{shoe.product}: {total_value}")

        print("\n")

    except Exception as e:
        print(f"An error occurred: {e}")

# Function for highest qty
def highest_qty():
    try:
        # Check if shoe list is empty
        if not shoe_list:
            print("No shoes to calculate value. ")
            return
        
        # Find the shoe with the highest quantity
        max_quantity_shoe = max(shoe_list, key= lambda x:x.quantity)

        # Print details of shoe with highest quantity
        print("\nShoe with the highest quantity: ")
        print(".............................")
        print(max_quantity_shoe)

        print("\nThis is shoe is for sale.\n")
    
    except Exception as e:
       print(f"An error occurred: {e}") 


read_shoes_data()  
'''
 line 194: Set a default read as the user requires this information for the functionality of the restock, value per item and highest quantity shoe function.  
'''

# Main Menu loop
while True:
    print("\n====Menu====")
    print("1. Capture Shoes")
    print("2. View all Shoes")
    print("3. Restock")
    print("4. Search Shoe")
    print("5. Value per Item")
    print("6. Highest Quantity Shoe")
    print("7. Exit")

    choice = input("Please enter your choice (1-8): ")

    if choice == "1":
        capture_shoes()
    elif choice == "2":
        view_all()
    elif choice =="3":
        re_stock()
    elif choice =="4":
        search_shoe()
    elif choice == "5":
        value_per_item()
    elif choice == "6":
        highest_qty()
    elif choice =="7":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")