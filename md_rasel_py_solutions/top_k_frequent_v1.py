# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 18:59:23 2025

@author: Md Rasel
"""
# Problem Statement: Given an integer array `nums` and an integer `k`,
# return the `k` most frequent elements within the array.

# Soln approach: counting the frequncy of each number in the given array
# using the dict get() method just like used in `valid anagram` problem.
# sorting them afterwards according to the frequency number.
# using pop() method, get the `k` most frequent number from sorted list
# Time complexity: O(n logn) 
# Space complexity: O(n) where n is the size of input array

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # empty dict for counting the freqency of each number
        freq_dict = {}
        # dict get(key,default) method 
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0) + 1
        # empty list for arranging the count of the numbers
        my_list = []
        for num, freq in freq_dict.items():
            my_list.append([freq,num])
        # sorting now will sort according to the frequency (ascending order)
        my_list.sort()

        # empty list for storing the final output : original numbers
        output = []
        # the idx 1 from the sorted array is the original number
        # using pop() method, get them. then append to output
        while len(output) < k:
            output.append(my_list.pop()[1])
        return output
    