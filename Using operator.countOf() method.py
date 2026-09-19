import operator as op

vowels="aeiouAEIOU"

def is_vowel(char):
    if op.countOf(vowels, char)>0:
        return True
    return False

print(is_vowel('a'))  # Output: True
print(is_vowel('b'))  # Output: False