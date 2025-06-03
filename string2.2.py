words = ["code", "edoc", "da", "d"]


def is_palindrome(word):
    return word == word[::-1] #True if word is same as its reverse, reverses the string


results = []

for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            combined = words[i] + words[j] 
            if is_palindrome(combined): #call function
                results.append((i,j))
print(results)

