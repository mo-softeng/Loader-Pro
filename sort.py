# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Adam Van De Visch, Mo Osman, Arushi Dutta, Sonia Haghgooie"

# Update "" with your team (e.g. T102)
__team__ = "T057"

#==========================================#
# Place your sort_characters_agility_bubble function after this line

def sort_characters_agility_bubble(character_list: list[dict], order: str)-> list[dict]:
    """Returns a list of dictionaries ordered in ascending or descending based on the 'Agility' attribute, given a list of dictionaries and a string 'A' or 'D'.
    Preconditions: List must contain dictionaries with key 'Agility', order = 'A' or 'B'
    >>>sort_characters_agility_bubble([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A")
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    >>>sort_characters_agility_bubble([{'Occupation':'EB'},{'Occupation': 'M'}], "A")
    'Agility' key is not present
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    >>>sort_characters_agility_bubble([{'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB','Agility': 52}, {'Occupation': 'AT', 'Agility': 7}], "D")
    [{'Occupation': 'EB', 'Agility': 52}, {'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'AT', 'Agility': 7}]
    """
    characters = len(character_list)
    key = True
    for i in character_list:
        if 'Agility' in i:
            key = True
        else:
            key = False
            break
    
    if order == "A" and key == True: 
        for character in range(characters - 1):
            for j in range(characters - 1):
                if character_list[j]['Agility'] > character_list[j + 1]['Agility']:
                    character_list[j], character_list[j + 1] = character_list[j + 1], character_list[j]
        return character_list
    
        
    elif order == "D" and key == True:
        for character in range(characters - 1):
            for j in range(characters - 1):
                if character_list[j]['Agility'] < character_list[j + 1]['Agility']:
                    character_list[j], character_list[j + 1] = character_list[j + 1], character_list[j]
        return character_list
            
            
            
    elif key == False:
        print("'Agility' key is not present")
        return character_list
    
    else:
        print('Invalid order string')
        
#==========================================#
# Place your sort_characters_intelligence_selection function after this line

def sort_characters_intelligence_selection(list_dics: list[dict], order: str) -> list[dict]:
    """
    return sorted list of dictionaries in accending/descending order based on the Intelligence key. 
    >>>  sort_characters_intelligence_selection([{'Occupation': 'EB','Intelligence': 3}, 
            {'Occupation': 'H','Intelligence': 1}], order: "A")
    >>> [{'Occupation': 'H', 'Intelligence': 1}, {'Occupation': 'EB', 'Intelligence': 3}]

    >>> sort_characters_intelligence_selection([{'Occupation': 'EB'}, {'Occupation': 'H','Intelligence': 1}], order: "A")
    >>> 'Intelligence' key is not present 
    [{'Occupation': 'EB'}, {'Occupation': 'H', 'Intelligence': 1}]

    >>> sort_characters_intelligence_selection([{'Occupation': 'EB', 'Intelligence': 12}, {'Occupation': 'H','Intelligence': 13}], order: "D")
    >>> [{'Occupation': 'H','Intelligence': 13}, {'Occupation': 'EB', 'Intelligence': 12}]
    """
    for i in range(len(list_dics)):
        try:
            if order == "A":  # Ascending low to high
                minimum_key = i
                for j in range(i + 1, len(list_dics)):
                    if list_dics[j]["Intelligence"] < list_dics[minimum_key]["Intelligence"]:
                        minimum_key = j
                list_dics[i], list_dics[minimum_key] = list_dics[minimum_key], list_dics[i]
            elif order == "D":  # Descending high to low
                maximum_key = i
                for j in range(i + 1, len(list_dics)):
                    if list_dics[j]["Intelligence"] > list_dics[maximum_key]["Intelligence"]:
                        maximum_key = j
                list_dics[i], list_dics[maximum_key] = list_dics[maximum_key], list_dics[i]
        except:
            print("'Intelligence' key is not present")
            return list_dics

    return list_dics

#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(characters: list[dict], order: str) -> list[dict]:
    """ Return a sorted list of characters in ascending or descending order based on health. 
    sort_characters_health_insertion.
    
    >>> sort_characters_health_insertion([{'Occupation': 'DB', 'Health': 62.15}, {'Occupation': 'M', 'Health': 63.56}], "A")
    [{'Occupation': 'DB', 'Health': 62.15}, {'Occupation': 'M', 'Health': 63.56}]
    >>>sort_characters_health_insertion([{'Occupation': 'HG', 'Health': 62.78}, {'Occupation': 'AT', 'Health': 62.15}], "A")
    [{'Occupation': 'HG', 'Health': 62.78}, {'Occupation': 'AT', 'Health': 62.15}]
    >>>sort_characters_health_insertion([{'Occupation':'HG'}, {'Occupation': 'DB'}], "A")
    "Health" key is not present.
    [{'Occupation': 'HG'}, {'Occupation': 'DB'}]

    """

    attribute_inlist = False
    
    for d in characters:
        if 'Health' in d:
            attribute_inlist = True 
        else:
            attribute_inlist = False
        if attribute_inlist == True:
            if order == "A":
                for i in range(len(characters)):
                    temp = (characters[i])
                    j = i - 1
                    while j >= 0 and temp["Health"] < (characters[j])["Health"]:
                        characters[j + 1] = characters[j]
                        j -= 1
                        characters[j + 1] = temp
            elif order == "D":
                for i in range(len(characters)):
                    temp = (characters[i])
                    j = i - 1
                    while j >= 0 and temp["Health"] > (characters[j])["Health"]:
                        characters[j + 1] = characters[j]
                        j -= 1
                        characters[j + 1] = temp
    if attribute_inlist == False:
        print('"Health" key is not present.')
    return characters

#==========================================#
# Place your sort_characters_armor_bubble function after this line

def sort_characters_armor_bubble(characters: list, order: str) -> list:

    """Returns a list of dictionaries sorted in either ascending or descending order (depending on user input) of character armor. Returns the original list if 'Armor' is not a key in the dicitonary provided.
    
    Parameters: All headers must exist in file, input string must be either 'A' or 'D'
    
    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 7}, {'Occupation': 'H', 'Armor': 12}, {'Occupation': 'AH', 'Armor': 9}], "D")
    [{'Occupation': 'H', 'Armor': 12}, {'Occupation': 'AH', 'Armor': 9}, {'Occupation': 'EB', 'Armor': 7}]
    
    >>>sort_characters_armor_bubble([{'Occupation': 'EB'}, {'Occupation': 'M'}], "D")
    "Armor" key is not present.
    [{'Occupation': 'EB'}, {'Occupation': 'M'}]
    
    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 14}, {'Occupation': 'H', 'Armor': 10}], "A")
    [{'Occupation': 'H', 'Armor': 10}, {'Occupation': 'EB', 'Armor': 14}]
    """
    
    armor_key = False
    
    for i in characters:
        if 'Armor' in i:
            armor_key = True
        else:
            break

    if order == 'A' and armor_key == True:
        swap = True
        while swap:
            swap = False            
            for i in range(len(characters) - 1):
                if characters[i]['Armor'] > characters[i + 1]['Armor']:
                    characters[i], characters[i + 1] = characters[i + 1], characters[i]
                    swap = True
        return characters

    elif order == 'D' and armor_key == True:
        swap = True
        while swap:
            swap = False            
            for i in range(len(characters) - 1):
                if characters[i]['Armor'] < characters[i + 1]['Armor']:
                    characters[i], characters[i + 1] = characters[i + 1], characters[i]
                    swap = True
        return characters

    else:
        print('"Armor" key is not present')
        return characters

#==========================================#
# Place your sort function after this line

def sort(character_list: list[dict], order: str, attribute: str)-> list[dict]:
    """Returns a sorted list of dictionaries given a list of dictionaries, the order of sorting, and the attribute to be sorted by.
    Preconditions: order == 'A' or 'D', attribute == 'Agility' or 'Health' or 'Intelligence' or 'Armor'
    >>>sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], 'A', 'Agility')
    [{'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 13}]
    >>>sort([{'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB','Agility': 52}, {'Occupation': 'AT', 'Agility': 7}], 'D', 'Luck')
    Invalid attribute
    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB', 'Agility': 52}, {'Occupation': 'AT', 'Agility': 7}]
    >>>sort([{'Occupation': 'EB','Agility': 13}, {'Occupation': 'H', 'Agility': 11}, {'Occupation': 'EB','Agility': 52}, {'Occupation': 'AT', 'Agility': 7}], 'W', 'Armor')
    Cannot be sorted by W
    """
    if order != 'A' and order != 'D':
        print('Cannot be sorted by ' + order)
    
    if order == 'A':
        if attribute == 'Agility':
            return sort_characters_agility_bubble(character_list, 'A')
        
        elif attribute == 'Intelligence':
            return sort_characters_intelligence_selection(character_list, 'A')
        
        elif attribute == 'Health':
            return sort_characters_health_insertion(character_list, 'A')
        
        elif attribute == 'Armor':
            return sort_characters_armor_bubble(character_list, 'A')        

    
    if order == 'D':
        if attribute == 'Agility':
            return sort_characters_agility_bubble(character_list, 'D')
        
        elif attribute == 'Intelligence':
            return sort_characters_intelligence_selection(character_list, 'D')
        
        elif attribute == 'Health':
            return sort_characters_health_insertion(character_list, 'D')
        
        elif attribute == 'Armor':
            return sort_characters_armor_bubble(character_list, 'D')      
        
    if attribute != 'Agility' and attribute != 'Intelligence' and attribute != 'Health' and attribute != 'Armor':
        print('Invalid attribute')
        return character_list





# Do NOT include a main script in your submission

