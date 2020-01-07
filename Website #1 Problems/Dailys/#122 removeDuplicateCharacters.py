from collections import Counter
def removeDuplicateCharacters(s):
    count = Counter(s)
    for letter in count.keys():
        if count[letter] != 1:
            s = s.replace(letter, "")
    return s
    