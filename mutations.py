def mutate_string(string, position, character):
    # Convert the string to a list to make the change
    string_list = list(string)
    
    # Change the character at the specified position
    string_list[position] = character
    
    # Convert the list back to a string
    result = ''.join(string_list)
    
    return result

