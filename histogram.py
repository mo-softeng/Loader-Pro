# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Adam Van De Visch"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297389"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-057"

#==========================================#
# Place your histogram function after this line

import matplotlib.pyplot as plt

def histogram(character_list: list[dict], plot_attribute: str):
    """Return a histogram which displays the number of characters who have different values that correlate to an attribute, given a list of dictionaries, and a desired attribute.
    Preconditions: plot_attribute == 'Strength' or 'Luck' or 'Agility' or 'Personality' or 'Occupation' or ''Weapon' or 'Stamina', or 'Intelligence' 
    >>>histogram([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Club'}], 'Strength')
    20
    >>>histogram([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Club'}], 'Weapon')
    -1
    >>>histogram([{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Club'}], 'Personality')
    13
    """
    attribute_list = []
    attribute_count= []
    attribute_increments = []
    list_count = []
    string = False
    
    try:
        for dictionary in character_list:
            entry = dictionary[str(plot_attribute)]
                
            if entry not in attribute_list:
                attribute_list.append(entry)
            
        for dictionary in character_list:
            entry = dictionary[str(plot_attribute)]
            attribute_count.append(entry)
            if type(entry) == str:
                string = True
            
        if string == True:
            dict_count = {}
                
            for attribute in attribute_list:
                dict_count[attribute] = 0
                    
            for attribute in attribute_count:
                dict_count[attribute] += 1
                    
            for count in dict_count:
                entry = dict_count[count]
                list_count.append(entry)
                    
        else:
            dict_count = {}
            
            increments = (max(attribute_list) - min(attribute_list)) / 20
            
            for increment in range(0,21):
                if increment < 19:
                    increment_range = min(attribute_list) + (increments * increment)
                    dict_count[increment_range] = 0
                    
                else:
                    increment_range = max(attribute_list)
                    dict_count[increment_range] = 0
                    
            for increment in range(0,21):
                if increment < 19:
                    increment_range = min(attribute_list) + increments * increment
                    min_range = (min(attribute_list) + increments * (increment - 1))
            
                    for attribute in attribute_list:
                        if (attribute <= increment_range) and (attribute > min_range):
                            dict_count[increment_range] += 1
                
                else:
                    increment_range = max(attribute_list)
                    min_range = min(attribute_list) + increments * (increment - 1)
            
                    for attribute in attribute_list:
                        if attribute <= increment_range and attribute > min_range:
                            dict_count[increment_range] += 1
                            
            for count in dict_count:
                entry = dict_count[count]
                list_count.append(entry)
            
            for count in dict_count:
                entry = (count)
                attribute_increments.append(entry)
        
        figure_1 = plt.figure()
        plt.title(str(plot_attribute) + ' Attribute Plot')
        plt.xlabel(str(plot_attribute))
        plt.ylabel('Characters')
            
        if string == False:
            plt.bar(attribute_increments, list_count, color = 'green')
            plt.show()
            return max(attribute_list)
            
        else:
            plt.bar(attribute_list, list_count, color = 'blue')
            plt.show()
            return -1

    
    except:
        print('The attribute ' + str(plot_attribute) + ' Does not exist')
    
# Do NOT include a main script in your submission
    

