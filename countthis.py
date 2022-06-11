def count(name:str) -> None:
    # Defining variables for future needs
    dictionary = {}
    dict_keys = []
    most_common = []
    second_common = []
    third_common = []
    name_lower = name.lower()
    
    # Making a dictionary with every character from the string and adding to the values if repeated
    for i in range(len(name)):
        if name_lower[i] not in dictionary and name_lower[i] != " ":
            dictionary[name_lower[i]] = 1
        elif name_lower[i] != " ":
            dictionary[name_lower[i]] = dictionary[name_lower[i]]+1
        else:
            continue
        
    # Sorting dictionary for easier approach
    dictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))
    
    # Appending to the array the last (and the most common) key from dictionary
    most_common.append(list(dictionary)[-1])
    
    # Appending others with the same value, if exist
    for i in dictionary:
        if dictionary[i] == dictionary[most_common[0]] and i != most_common[0]:
            most_common.append(i)
        else:
            continue
    
    # Sorting for alphabetical purposes only
    most_common = sorted(most_common)
    
    # Beggining of the end: tree of conditions
    if len(most_common) >= 3:
        dict_keys = [most_common[0], most_common[1], most_common[2]]
    elif len(most_common) == 2:
        # Searching for the first key from the end to be smaller than most common element
        for n in range(-1,-len(dictionary), -1):
            if dictionary[list(dictionary)[n]] < dictionary[most_common[0]]:
                second_common.append(list(dictionary)[n])
                break
            else:
                continue
        # Same thing all over again but for every condition that may occure
        for i in dictionary:
            if dictionary[i] == dictionary[second_common[0]] and i != second_common[0]:
                second_common.append(i)
            else:
                continue
        second_common = sorted(second_common)
        dict_keys = [most_common[0], most_common[1], second_common[0]]
    elif len(most_common) == 1:
        for n in range(-1,-len(dictionary), -1):
            if dictionary[list(dictionary)[n]] < dictionary[most_common[0]]:
                second_common.append(list(dictionary)[n])
                break
            else:
                continue
        for i in dictionary:
            if dictionary[i] == dictionary[second_common[0]] and i != second_common[0]:
                second_common.append(i)
            else:
                continue
        second_common = sorted(second_common)
        if len(second_common) != 2:
            for n in range(-1, -len(dictionary), -1):
                if dictionary[list(dictionary)[n]] < dictionary[second_common[0]]:
                    third_common.append(list(dictionary)[n])
                    break
                else:
                    continue
            for i in dictionary:
                if dictionary[i] == dictionary[third_common[0]] and i != third_common[0]:
                    third_common.append(i)
                else:
                    continue
            third_common = sorted(third_common)
            dict_keys = [most_common[0], second_common[0], third_common[0]]
        else:
            dict_keys = [most_common[0], second_common[0], second_common[1]]
            
    # Giving the results
    print(f"Your string is: {name}")
    print(f"Most common letters in this string are: \'{dict_keys[0]}\', \'{dict_keys[1]}\' and \'{dict_keys[2]}\'.")

if __name__ == "__countthis__":
    # Uncomment if you want some interaction
    #name = input("Please provide your string for count: ")
    count(name="ababagalamaga")