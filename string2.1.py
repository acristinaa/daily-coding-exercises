w = "ab"
s = "abxaba"

def is_anagram(w,s):
    result = [] # Create an empty list to store the starting positions of anagrams
    for i in range(len(s) - len(w) + 1):# Loop over all possible starting positions in s where an anagram of w could fit, len(s) - len(w) + 1 ensures we don't go past the end of the string
        window =  s[i:i+len(w)] # Get the current "window" of letters in s, starting at position i
        if sorted(window) == sorted(w):  # Check if the letters in the window form an anagram of w
            result.append(i) # If it's an anagram, add the starting position i to the result list
    print(result)

is_anagram(w,s)