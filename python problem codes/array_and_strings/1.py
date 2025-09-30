# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of 
# the merged string.
# Return the merged string.

def merge_alternately(word1, word2):
    merged = []
    len1, len2 = len(word1), len(word2)
    min_len = min(len1, len2)
    
    # Add alternating characters
    for i in range(min_len):
        merged.append(word1[i])
        merged.append(word2[i])
    
    # Append the remaining part of the longer string
    if len1 > len2:
        merged.append(word1[min_len:])
    else:
        merged.append(word2[min_len:])
    
    return ''.join(merged)


