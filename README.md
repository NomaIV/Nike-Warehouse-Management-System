# Nike Warehouse Management System

This OOP capstone project simulates a Nike warehouse management system using Python. It allows store managers to perform stock-taking, optimise delivery times, and manage inventory efficiently.

## Project Overview
As a store manager for a Nike warehouse, you can use this Python program to:
- Search products by code.
- Determine and restock products with the lowest quantity.
- Identify products with the highest quantity for sale.
- Calculate the total value of each stock item based on cost and quantity.

The program reads data from `inventory.txt`, processes it, and provides interactive menu options to perform these tasks.

## Features
- **Search by Code:** Find detailed information about a product using its code.
-  **Restock:** Automatically identify and restock products with the lowest quantity.
- **Highest Quantity:** Identify products with the highest quantity available for sale.
- **Value Calculation:** Calculate the total value of each stock item using the formula `value = cost * quantity`.

## Technologies Used
- Python
- Docker
- SQLite (for `inventory.txt` storage)
- Tabulate (optional, for organised data display)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/NomaIV/nike-warehouse.git
   cd L1T30
   ```

2. Install dependencies using pip:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the program:
   ```bash
   python3 inventory.py
   ```

## Usage
1. **Menu Options:**
   - `1`: Capture Shoes
   - `2`: View all Shoes
   - `3`: Restock
   - `4`: Search Shoe
   - `5`: Value per Item
   - `6`: Highest Quantity Shoe
   - `7`: Exit

2. To run the program, execute `python3 inventory.py` in your terminal or command prompt. This will start the program and display the menu options.

3. Enter the corresponding number (1-7) for the action you want to perform and follow the on-screen prompts.

4. Example: If you choose `1`, it will prompt you to capture shoe details. Choosing `2` will display all stored shoes, and so on.

5. To exit the program, enter `7` at the prompt.

## File Structure

- `inventory.py`: Main program file containing menu options and logic.
- `inventory.txt`: Text file storing data about Nike products.
- `requirements.txt`: File listing Python dependencies.
- `Dockerfile`: Docker configuration file for containerisation (optional).

## License
This project is licensed under the MIT License.
