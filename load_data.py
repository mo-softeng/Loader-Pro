# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Mohammed Osman, Adam Van De Visch, Sonia Haghgooie, Arushi Dutta"

# Update "" with your team (e.g. T102)
__team__ = "T57"


#==========================================#
# Place your character_occupation_list function after this line
def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """ return the specific occupation type of a file. 
    Preconditions:    
    1.Text file must contain data in CSV format.
    2.file_name, and occupation_name must be strings
    3.The file_name must exist in the same directory as the code file
    >>> character_occupation_list ('characters-mat.csv', 'AT')
    [
        ...
    ,{'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 
    'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 
    'Weapon': 'Staff'},
        ...
    ]
    >>> character_occupation_list ('characters-mat.csv', 'DB')
    [
        ...
    ,{'Strength': 14, 'Agility': 14, 'Stamina': 3, 'Personality': 17, 
    'Intelligence': 9, 'Luck': 0.56, 'Armor': 12, 
    'Weapon': 'Staff'},
        ...
    ]
    >>> character_occupation_list ('characters-mat.csv', 'XX')
    []
    """
    take_header = False
    header = ""
    data = []
    in_file = open(file_name, "r")
    for line in in_file:
        line = line.strip('\n').split(",")
        if not take_header:
            header = line
            take_header = True
        elif line[0] == occupation:
            datadic = {}
            for i in range(1, 9):
                if i == 6:
                    datadic[header[i]] = float(line[i])
                elif i == 8:
                    datadic[header[i]] = str(line[i])
                else:
                    datadic[header[i]] = int(line[i])
            data.append(datadic)
    in_file.close()

    return data

#==========================================#
# Place your character_strength_list function after this line
def character_strength_list(file_name: str, strength_range: tuple) -> list[dict]:
    """Return a list of characters (stored as a dictionary), read from file_name, whose strength falls between the minimum and maximum values, inclusive, that were provided as an input parameter. 

    Precondition: file has all headers
    
    >>>character_strength_list("characters-mat.csv", (17, 18))
    [{'Occupation': 'AT', 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11, 'Weapon': 'Club'}, {'Occupation': 'AT', 'Agility': 10, 'Stamina': 7, 'Personality': 10, 'Intelligence': 12, 'Luck': 0.83, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'AT', 'Agility': 7, 'Stamina': 8, 'Personality': 12, 'Intelligence': 7, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Axe'}, {'Occupation': 'DB', 'Agility': 5, 'Stamina': 10, 'Personality': 11, 'Intelligence': 11, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Club'}, 
    ... {'Occupation': 'WA', 'Agility': 13, 'Stamina': 2, 'Personality': 12, 'Intelligence': 6, 'Luck': 0.56, 'Armor': 11, 'Weapon': 'Dagger'}, {'Occupation': 'WA', 'Agility': 8, 'Stamina': 8, 'Personality': 11, 'Intelligence': 4, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Dagger'}]

    >>>character_strength_list("characters-mat.csv", (3, 5))
    []
    
    >>>character_strength_list("characters-mat.csv", (20, 34))
    [{'Occupation': 'AT', 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10, 'Weapon': 'Staff'}, {'Occupation': 'DB', 'Agility': 7, 'Stamina': 9, 'Personality': 13, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Club'}, ... {'Occupation': 'VF', 'Agility': 6, 'Stamina': 8, 'Personality': 8, 'Intelligence': 11, 'Luck': 0.39, 'Armor': 9, 'Weapon': 'Dagger'}]
    """

    in_file = open(file_name, "r")
    strength_list = []
    first_line = True

    for line in in_file:
        line = line.strip().split(",")

        if first_line:
            header = line
            first_line = False
        else:
            if int(line[1]) <= max(strength_range) and int(line[1]) >= min(strength_range):
                character = {}
                character[header[0]] = str(line[0])
                character[header[2]] = int(line[2])
                character[header[3]] = int(line[3])
                character[header[4]] = int(line[4])
                character[header[5]] = int(line[5])
                character[header[6]] = float(line[6])
                character[header[7]] = int(line[7])
                character[header[8]] = str(line[8])
    
                strength_list.append(character)

    in_file.close()
    return strength_list

#==========================================#
# Place your character_luck_list function after this line
def character_luck_list (file_name: str, luck:float) -> list[dict]:
    """ 
    Return a list of dictionaries that contains all the charaacters and their data, that have a luck that is less than the specified float value. 
    
    Precondition: file_name has the columns ['occupation', 'strength', 'agility', 'stamina', 'personality', 'intellligence', 'armor', 'weapon'] and luck must be less than 1.
    
    >>> character_luck_list ('characters-mat.csv', 0.4)
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7,
    'Personality': 13, 'Intelligence': 11, 'Armor': 8, 'Weapon': 'Staff'},
    {'Occupation': 'AT', 'Strength': 19, 'Agility': 9, 'Stamina': 9,
    'Personality': 10, 'Intelligence': 12, 'Armor': 10, 'Weapon': 'Dagger'},
    {another element},
    …
    ]
    
    >>> character_luck_list ('characters-mat.csv', 0.1)
    []
    """
    in_file = open(file_name, 'r')

    luck_list = []
    line_1 = True 
    for line in in_file:
        character_dic = {}
        line = line.strip('\n').split(',')
        if line_1: 
            line_1 = False
            header = line    
        else:
            if float(line[6]) < luck:
                for i in range (0,len(header)):
                        if i == 6: 
                            character_dic[header[i]] = float(line[i])
                        elif i == 0 or i == 8:
                            character_dic[header[i]] = str(line[i])
                        else:
                            character_dic[header[i]] = int(line[i])
                character_dic.pop("Luck")
                luck_list.append(character_dic)
    return luck_list                   
            

#==========================================#
# Place your character_weapon_list function after this line
def character_weapon_list(file1: str, weapon: str)-> list:
    """Return a dictionary containing all stats except the weapon type of a character, of all characters using a specific weapon and a file containing characters.
    >>>character_weapon_list('characters-mat.csv', "Staff")
    [{'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 8, 'Personality': 8, 'Intelligence': 15, 'Luck': 0.72, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 20, 'Agility': 7, 'Stamina': 2, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 10},  {'Occupation': 'AT', 'Strength': 13, 'Agility': 5, 'Stamina': 5, 'Personality': 7, 'Intelligence': 12, 'Luck': 0.5, 'Armor': 9},
    ...
    ]
    >>>character_weapon_list('characters-mat.csv', "Dagger")
    [{'Occupation': 'AT', 'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9}, {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 16, 'Agility': 8, 'Stamina': 8, 'Personality': 7, 'Intelligence': 9, 'Luck': 0.94, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 13, 'Agility': 8, 'Stamina': 8, 'Personality': 6, 'Intelligence': 10, 'Luck': 0.72, 'Armor': 10}, 
    ...
    ]
    >>>character_weapon_list('characters-mat.csv', "Gun")
    []
    """
    file = open(file1, 'r')
    weapon_list = []
    first_line = True
    for line in file:
        line = line.strip().split(',')
        if first_line == True:
            header = line
            first_line = False
        else:
            data_set = {
                header[0]: line[0],
                header[1]: int(line[1]),
                header[2]: int(line[2]),
                header[3]: int(line[3]),
                header[4]: int(line[4]),
                header[5]: int(line[5]),
                header[6]: float(line[6]),
                header[7]: int(line[7])}
            if line[8] == weapon:
                weapon_list.append(data_set)
    file.close()
    return weapon_list

#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, pair_values: tuple) -> list[dict]:
    """Return specific loaded data based on a tuple of entry provided. 

    Precondition: file name must have headings: "Occupation", "Strength", "Agility", "Stamina", "Personality", "Intelligence", "Luck", "Armor", and "Weapon"

    >>>load_data('characters-mat.csv', ('Occupation', 'H'))
    [... 
    {'Strength': 20, 'Agility': 6, 'Stamina': 7, 'Personality': 7, 'Intelligence': 10, 'Luck': 0.72, 'Armor': 9, 'Weapon': 'Club'},
    ...]
    >>>load_data('characters-mat.csv', ('Agility', 24))
    []
    >>>load_data('characters-mat.csv', ('Weapon', 'Sling'))
    [...
    {'Occupation': 'EB', 'Strength': 11, 'Agility': 6, 'Stamina': 14, 'Personality': 11, 'Intelligence': 8, 'Luck': 0.44, 'Armor': 9},
    ...] 
    """
    data = []
    file_read = open(file_name, "r")
    header_found = False
    header = ""
    if pair_values[0] == "All":
        for line in file_read:
            line = line.strip().split(",")
            if not header_found:
                header = line
                header_found = True
            else:
                dic = {}
                for i in range(9):
                    if i == 0 or i == 8:
                         dic[header[i]] = str(line[i])
                    elif i == 6:
                         dic[header[i]] = float(line[i])
                    else:
                         dic[header[i]] = int(line[i])
                data.append(dic)
        return data
    elif pair_values[0] == "Strength":
        return character_strength_list(file_name, pair_values[1])
    elif pair_values[0] == "Luck":
        return character_luck_list(file_name, pair_values[1])
    elif pair_values[0] == "Weapon":
        return character_weapon_list(file_name, pair_values[1])
    elif pair_values[0] == "Occupation":
        return character_occupation_list(file_name, pair_values[1])
    else:
        print("Invalid Value")
        return data

        
#==========================================#
# Place your calculate_health function after this line
def calculate_health(list_dics: list[dict]) -> list[dict]:
    """
    Returns a list of dictionaries with an added health stat, given a list of dictionaries,all of which each contains a strength, agility, personality, intelligence, stamina, armor, and luck stat.
    Preconditions: Each dictionary must include a strength, agility, personality, intelligence, stamina, armor, and luck stat.
    >>>calculate_health(load_data('characters-mat.csv', ('Weapon', 'Dagger')))
    [{'Occupation': 'AT', 'Strength': 7, 'Agility': 5, 'Stamina': 9, 'Personality': 12, 'Intelligence': 14, 'Luck': 0.78, 'Armor': 9, 'Health': 110.18}, {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 12, 'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Health': 92.0},
    ...
    ]
    >>>calculate_health(load_data('characters-mat.csv', ('Occupation', 'DB')))
    [{'Strength': 17, 'Agility': 5, 'Stamina': 10, 'Personality': 11, 'Intelligence': 11, 'Luck': 0.67, 'Armor': 9, 'Weapon': 'Club', 'Health': 108.27000000000001}, {'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 13, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10, 'Weapon': 'Club', 'Health': 99.0},
    ...
    ]
    >>>calculate_health(load_data('characters-mat.csv', ('All', -23)))
    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'Health': 78.88}, {'Occupation': 'AT', 'Strength': 12, 'Agility': 3, 'Stamina': 7, 'Personality': 13, 'Intelligence': 11, 'Luck': 0.33, 'Armor': 8, 'Weapon': 'Staff', 'Health': 67.12},
    ...
    ]
    """
    health = 0
    for dic in list_dics:
        health = (int(dic["Strength"]) + int(dic["Agility"]) + int(dic["Personality"]) + int(dic["Intelligence"]) + int(dic["Stamina"])) + (int(dic["Armor"]) ** 2 * float(dic["Luck"]))
        dic["Health"] = health
    return list_dics
# Do NOT include a main script in your submission

d = load_data("characters-test.csv", ("Luck", 0.6))
print(d)