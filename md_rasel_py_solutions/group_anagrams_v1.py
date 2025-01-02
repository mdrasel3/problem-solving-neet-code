"""
Created on Wed Jan  1 19:10:13 2025

@author: Md Rasel
"""
# Problem Statement : Given an array of strings `strs`, group all anagrams
# together into sublists. You may return the output in any order.

# Soln approach: create empty dict, sort each string and use them as key
# in the dict. use setdefault(key,[]), since key is not in the dict.
# in our dict, (key,value) == (sorted strings, list of original strings)
# therefore, we need to return the value of the dict.
# Time complexity: O(m*n logn) where m=total number of strings in `strs`
# and n=avg length of each string, for sorting nlogn
# Space complexity: m*n

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        for each_str in strs:
            sorted_strings = ''.join(sorted(each_str))
            dict_strs.setdefault(sorted_strings,[]).append(each_str)
        return dict_strs.values()