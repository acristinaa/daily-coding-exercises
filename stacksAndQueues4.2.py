def are_brackets_balanced(stacky):
    stack = []
    bracket_pairs = { #Create dictionary
        ")" : "(",
        "]" : "[",
        "}" : "{",
    }

    for char in stacky:
        if char == "(" or char == "[" or char == "{": #If the character is an opening bracket, push it onto the stack
            stack.append(char)

        elif char == ")" or char == "]" or char == "}": #If the character is a closing bracket, check if it matches the most recent opening bracket
            if not stack:
                return False
            last_open_bracket = stack.pop() 

            if bracket_pairs[char] != last_open_bracket: #Check if the closing bracket matches the opening bracket we just popped
               return False
            
    return len(stack) == 0   #If stack is empty (length 0), all brackets were balanced; otherwise, some were left open

            
print(are_brackets_balanced("( [ ] ) [ ] ( { } )")) # This should print True
print(are_brackets_balanced("( [  ) ]")) # This should print False
print(are_brackets_balanced("( ( ( )")) # This should print False