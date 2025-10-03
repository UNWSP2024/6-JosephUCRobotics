# Author: Joseph Kracht
# Last Modified: 10/3/2025
# Title: Tax Rate

# Program #3: Tax Rate
# A retail company must file a monthly sales tax report listing the total sales for the month,
# and the amount of state and county sales tax collected.
# The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent.
# Write a program that asks the user to enter the total sales for the month.
# From this figure, the application should calculate and display the following:

# The amount of county sales tax.
# The amount of state sales tax.
# The total sales tax (county plus state)
# Use at least one function with input and output in this program

def calc_county_tax(sales):
    county_tax = sales * 0.025
    return county_tax

def calc_state_tax(sales):
    state_tax = sales * 0.05
    return state_tax

# Get sales
total_sales = float(input("Enter the total sales for the month: "))

# Calc total sales tax
total_sales_tax = calc_county_tax(total_sales) + calc_state_tax(total_sales)

# Display
print("The total sale for the month is $",total_sales)
print("The amount of county sails tax is $", calc_county_tax(total_sales))
print("The amount of state sails tax is $", calc_state_tax(total_sales))
print("The total sales tax is $",total_sales_tax)
