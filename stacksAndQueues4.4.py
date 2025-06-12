import itertools #Importing the itertools module to use permutations

def generate_all_orders(n): #This function generates all possible orderings (permutations) of the numbers 0 to n-1
    return list(itertools.permutations(range(n))) #Returns a list of all permutations of [0, 1, ..., n-1]


def matches_clues(perm,clues): #This function checks if a given permutation matches the list of clues
    for i in range(1, len(clues)): #Start from the second element (index 1) because clues[0] is always None
        if clues[i] == '+': #If the clue says "next number should be bigger"
            if not perm[i] > perm[i - 1]: #Check if the current number is actually greater than the previous
                return False
        elif clues[i] == '-': #If the clue says "next number should be smaller"
            if not perm[i] < perm[i - 1]: #Check if the current number is smaller than the previous
                    return False
    return True #If all clues are matched, return True

def find_matching_order(clues): #This function finds the first permutation that matches the clue pattern
     n = len(clues) #The number of numbers we need to arrange
     for perm in generate_all_orders(n): #Try each possible permutation
          if matches_clues(perm, clues): #Check if it matches the clues
               return list(perm) #If it does, return it as a list
     return None #If no permutation matches, return None
          
     


perm = (0,2,1)
clues = [None, '+', '-']


print("Orders: ", generate_all_orders(3))

print("Matches: ", matches_clues(perm, clues))

print("Result: ", find_matching_order(clues))
