from collections import Counter

def find_anagram(word, anagram):
    return Counter(word) == Counter(anagram)


# Testing solution.
print(find_anagram("hello","check"))
print(find_anagram("below","elbow"))
