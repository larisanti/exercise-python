"""
Curso:
Learn Python 3 (Codecademy)

Objetivo:
Praticar variáveis, concatenação e formatação de strings.
"""

# Store the names and prices of a furniture store’s catalog in variables.
# Then process the total price and item list of customers, 
# printing them to the output terminal.

# Create variable for first item
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Create variable for price
lovely_loveseat_price = 254.00

# Create variable for adding new characteristic
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

# Create variable for price
stylish_sette_description = 180.50

# Create variable for another item
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

# Create variable for price
luxurious_lamp_price = 52.15

# Create a variable for tax
sales_tax = .088

# Create variable for costumer1
customer_one_total = 0

# Create a variable to make a list of the things bought
customer_one_itemization = ""

# Update total considering that the costumer bought the Lovelyseat
customer_one_total = lovely_loveseat_price
custumer_one_itemization = lovely_loveseat_description

# Also bought Luxurious Lamp
customer_one_total = lovely_loveseat_price + luxurious_lamp_price
customer_one_itemization = lovely_loveseat_description + luxurious_lamp_description
print(customer_one_total)

# Add taxes
customer_one_tax = customer_one_total * sales_tax
print(customer_one_tax)

# Add total with tax
customer_one_total = customer_one_total + customer_one_tax
print(customer_one_total)

## Create receipt
# Create heading for Items
print("Customer One Items:")
print(customer_one_itemization)
# Create heading for Total
print("Customer One Total:")
print(customer_one_total)

