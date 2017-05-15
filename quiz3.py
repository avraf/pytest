# An anagram is a word obtained by rearranging the letters of another word. For example,
# "rats", "tars", and "star" are anagrams of one another, as are "dictionary" and
# "indicatory". We will call any list of single-word anagrams an anagram group. For
# instance, ["rats", "tars", "star"] is an anagram group, as is ["dictionary"].

# Write a method combine_anagrams(words) that, given a list of string words, groups the
# input words into anagram groups. Case doesn't matter in classifying strings as
# anagrams (but case should be preserved in the output), and the order of the anagrams
# in the groups doesn't matter. The output should be a list of anagram groups (i.e. a
# list of lists).

# Code skeleton:

def combine_anagrams(words):
    pass

# Example test case:

input = ['cars', 'for', 'potatoes', 'racs', 'four', 'scar', 'creams', 'scream']
output = [ ["cars", "racs", "scar"],
          ["four"],
          ["for"],
          ["potatoes"],
          ["creams", "scream"] ]
# Hint: You can quickly tell if two words are anagrams by sorting their letters, keeping
# in mind that upper vs. lowercase doesn't matter.
