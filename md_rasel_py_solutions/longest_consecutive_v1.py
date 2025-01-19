# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 13:07:14 2025

@author: Md Rasel
"""
# Problem Statement: Given an array of integers `nums`, return the length of the 
# longest consecutive sequence of elements that can be formed.


class Solution:
    def longestConsecutive(self,nums) -> int:
        numset = set(nums)
        longest_seq = 0

        for num in numset:
            if num-1 in numset:
                continue
            count_seq = 0
            while num in numset:
                count_seq += 1
                num += 1                
            longest_seq = max(longest_seq, count_seq)    
        return longest_seq