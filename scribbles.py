
import pytest

def vowels(word):
    number_of_vowels = 0
    the_vowels = ["a", "e", "i", "o", "u"]
    for letter in word.lower():
        if letter in the_vowels:
            number_of_vowels += 1
    return number_of_vowels


import pdb
a = "aaa"
b = "bbb"
c = "ccc"

def final(var1,var2,var3):
    pdb.set_trace()
    return(var1+var2+var3)

print(final(a,b,c))

