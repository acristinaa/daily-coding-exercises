word = "daily"

def word_swap():
    k = 1
    n = len(word) 
    smallest = word  #start with the original word as the smallest

    for i in range(n):
        rotated = word[i:] + word[:i]  #rotate the word
        if rotated < smallest:  #is this rotation better?
            smallest = rotated  #update if so

    print(smallest) 

word_swap()