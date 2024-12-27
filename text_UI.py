# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Mohammed Osman"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101312104"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-57"

#==========================================#
# Place your script for your text_UI after this line
from sort import *
from load_data import *
from histogram import *
from curve_fit import *

PROMPT1 = """
The available commands are:
    L)oad Data
    S)ort Data
    C)urve Fit
    H)istogram
    E)xit

Please type your command:
"""
PROMPT2 = """
Please enter the attribute you want to use for sorting:
'Agility', 'Armor', 'Intelligence', 'Health'
:
"""
data = None
halt_program = False
while not halt_program:
    user_choice = input(PROMPT1).upper()
    if user_choice == "L": #load data
        file_name = input("Please enter the name of the file: ")
        atribute = input("Please enter the attribute to use as a filter:")
        if atribute not in ["Strength", "Occupation", "Luck", "Weapon", "All"]:
            print("Invalid value")
            continue
        elif atribute != "All":
            value_of_atribute = input("Please enter the value of the attribute: ")
            if atribute == "Luck":
                value_of_atribute = float(value_of_atribute)
            elif atribute == "Strength":
                value_of_atribute = (int(value_of_atribute.strip("()").split(",")[0]), int(value_of_atribute.strip("()").split(",")[1]))
            try:
                data = calculate_health(load_data(file_name, (atribute, value_of_atribute)))
                print("Data loaded")
            except KeyError:
                data = load_data(file_name, (atribute, value_of_atribute))
                print("health can not be calculated")
                print("Data loaded")
        elif atribute == "All":
            data = calculate_health(load_data(file_name, (atribute, "")))
            print("Data loaded")


    elif user_choice == "S": #sort data
        sort_attribute = input(PROMPT2)

        while sort_attribute not in ('Agility', 'Armor', 'Intelligence', 'Health'):
            sort_attribute = input(PROMPT2)

        order_of_sort = input("Ascending (A) or Descending (D) order: ")
        if order_of_sort not in ["A", "D"]:
            print("Invalid command")
            continue
        if data == None:
            print("File not loaded. Please, load a file first.")
            continue
        else:
            data = sort(data, order_of_sort, sort_attribute)
        display_data = input("Data Sorted. Do you want to display the data? (Y/N): ").upper()
        if display_data == "Y":
            print(data)
        elif display_data == "N":
            continue

    elif user_choice == "C":
        fit_attribute = input("Please enter the attribute you want to use to find the best fit for Health: ")
        if fit_attribute not in ["Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck"]:
            print("Invalid command")
            continue
        order_poly = int(input("Please enter the order of the polynomial to be fitted: "))
        if data == None: 
            print("File not loaded. Please, load a file first.")
            continue
        else:
            print(curve_fit(data, fit_attribute, order_poly))


    elif user_choice == "H":
        his_attribute = input("Please enter the attribute you want to use for plotting: ")
        if his_attribute not in ["Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Weapon"]:
            print("Invalid command")
            continue
        elif data == None:
            print("File not loaded. Please, load a file first.")
            continue
        else:
            histogram(data, his_attribute)
        
    elif user_choice == "E": #exist program
        halt_program = True

    else:
        print("Invalid command")
    