"""
Given an array of strings, return all groups of strings that are anagrams.
Represent a group by a list of integers representing the index in the original list.
Look at the sample case for clarification.

 Anagram : a word, phrase, or name formed by rearranging the letters of another, such as 'spar', formed from 'rasp'
 Note: All inputs will be in lower-case.

input : cat dog god tca
Output : [[1, 4], [2, 3]]
cat and tca are anagrams which correspond to index 1 and 4.
dog and god are another set of anagrams which correspond to index 2 and 3.
The indices are 1 based ( the first element has index 1 instead of index 0).
"""
from collections import Counter


# @param A : tuple of strings
# @return a list of list of integers
def anagrams(A):
    n = len(A)
    result = []
    index_covered = set()
    for i in range(n):
        if i + 1 in index_covered:
            continue
        curr_set = [i + 1]
        index_covered.add(i + 1)
        chars = dict(Counter(A[i]))
        for j in range(i + 1, n):
            if j + 1 in index_covered:
                continue
            new_chars = dict(Counter(A[j]))
            if chars == new_chars:
                curr_set.append(j + 1)
                index_covered.add(j + 1)
        result.append(curr_set)
    return result
