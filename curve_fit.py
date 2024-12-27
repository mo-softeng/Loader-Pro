# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Arushi Dutta"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101296217"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-057"

#==========================================#
# Place your curve_fit function after this line

import numpy as np

def curve_fit(input_list: list, attribute: str, poly_order: int) -> str:

    """Return a string representation of the equation of the polynomial of best fit for the specified attribute and order.  
    
    Preconditions: attribute must be a key in the dictionaries provided, health must be a key in the dictonaries provided
    
    Precondition: 1 <= polynomial_order <= 5
    
    >>>curve_fit([{'Strength': 3, 'Health': 7}, {'Strength': 4, 'Health': 9}, {'Strength': 1, 'Health': 8}, {'Strength': 6, 'Health': 12}, {'Strength': 2, 'Health': 12}], 'Strength', 4)
    -0.72x^4+9.83x^3+-45.58x^2+82.67x+-38.2
    >>>curve_fit([{'Strength': 3, 'Health': 7}, {'Strength': 4, 'Health': 9}, {'Strength': 1, 'Health': 8}], 'Strength', 6)
    0.83x^2+-3.83x+11.0
    >>>curve_fit([{'Agility': 13, 'Health': 8}, {'Agility': 13, 'Health': 10}, {'Agility': 10, 'Health': 6}], 'Agility', 3)
    4.0x^1+-34.0
    """
    
    temp_dict = {}

    for item in input_list:
        attribute_value = item[attribute]
        health_value = item['Health']
        if item[attribute] not in temp_dict:
            temp_dict[attribute_value] = [health_value]
        else:
            temp_dict[attribute_value].append(health_value)

    final_dict = {}

    for key in temp_dict:
        lst = temp_dict[key]
        summation = 0
        for i in lst:
            summation += i
        average = summation / len(lst)
        final_dict[key] = average

    x_values = list(final_dict)
    y = final_dict.values()
    y_values = []
    for j in y:
        y_values.append(j)

    inter_order = len(x_values) - 1

    if poly_order <= len(x_values):
        coef = np.polyfit(x_values, y_values, poly_order)
        degree = poly_order

    else:
        coef = np.polyfit(x_values, y_values, inter_order)
        degree = inter_order

    order = len(coef) - 1

    equation = ''
    for i in coef:
        if order == len(coef) - 1:
            equation += str(round(i, 2)) + "x^" + str(order)
        elif order > 1:
            equation += "+" + str(round(i, 2)) + "x^" + str(order)
        elif order == 1:
            equation += "+" + str(round(i, 2)) + "x"
        elif order == 0:
            equation += "+" + str(round(i, 2))
        order -= 1

    return equation


# Do NOT include a main script in your submission

