def findOccurences(s, ch):
    return [i for i, letter in enumerate(s) if letter == ch]


print findOccurences("abbaa", "a")
