"""
Created on Wed Jan  1 18:34:04 2025

@author: Md Rasel
"""
# Problem Statement: Given two strings `s` and `t`, return `true` if 
# the two strings are anagrams of each other, otherwise return `false`.
# An anagram is a string that contains the exact same characters as
# another string, but the order of the characters can be different.

# Soln approach: check if the length of two strings is equal or not
# using hashmap aka dict in python, track the frequency of each `char`
# if the frequency of both strings matches, then it is anagram
# Time complexity: O(n+m) where n=len(s) and m= len(t)
# Space complexity: O(1) since we have 26 characters

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the length of s and t is not equal, not anagram
        if len(s) != len(t): return False 
        # frequency dict for both strings 
        freq_s = {} 
        freq_t = {} 
        # dict get(key,default) method 
        for char in s: 
            freq_s[char] = freq_s.get(char, 0) + 1 
        for char in t: 
            freq_t[char] = freq_t.get(char, 0) + 1 
        
        # compare the frequency dict, if true -> anagram
        return freq_s == freq_t