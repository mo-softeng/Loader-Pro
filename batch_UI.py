# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Sonai Haghgooie"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306866"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-057"

#==========================================#
# Place your script for your batch_UI after this line
from load_data import *
from sort import *
from curve_fit import curve_fit
from histogram import histogram

# Asks user what file to read from
file_name = input("Please enter the name of the file: ")
Uncut_data = ""
batch_file = open(file_name, 'r')

for line in batch_file:
    line = line.strip('\n')
    Uncut_data = Uncut_data + line + ";"

batch_file.close()
data = Uncut_data.split(";")
data = data[:-1]

if data[0].lower() != 'e':
    for i in range(0, len(data)):
        print(data[i], len(data))
        # if theres a line for load data
        if data[i].lower() == 'l':
            loaded_data = load_data(data[i + 1], (data[i + 2], data[i + 3]))
            current_data = calculate_health(loaded_data)
            print("data loaded")
            
        if data[i].lower() == 's':
            if data[i + 1] == 'Agility':
                sorted_data = sort_characters_agility_bubble(current_data, data[i + 2])
            if data[i + 1] == 'Armor':
                sorted_data = sort_characters_armor_bubble(current_data, data[i + 2])
            if data[i + 1] == 'Intelligence':
                sorted_data = sort_characters_intelligence_selection(current_data, data[i + 2])
            if data[i + 1] == 'Heart':
                sorted_data = sort_characters_health_insertion(current_data, data[i + 2])
            current_data = sorted_data

            if data[i + 3].lower() == 'y':
                print(current_data)
                
        if data[i].lower() == 'c':
            curve_equation = curve_fit(current_data, data[i + 1], data[i + 2])
            print(curve_equation)

        if data[i].lower() == 'h' and len(data[i + 1]) > 1:
            histogram_plot = histogram(current_data, data[i + 1])
            print(histogram_plot)
    