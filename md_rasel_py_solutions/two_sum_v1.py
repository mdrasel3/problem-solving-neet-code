"""
Created on Dec  16 19:45:45 2024
@Author: Md. Rasel
"""
# Problem Statement: Given an array of integers `nums` and integer `target`, return indices 
# `i` and `j` such that `nums[i] + nums[j] == target` and `i != j`.
# You may assume that every input has exactly one pair of indices `i` and `j`
# that satisfy the condition.

# Soln approarch: maintain a mapping from each number to its index.
# Check if (target -  nums[i]) has already been found.
# Time complexity: O(n)
# Space complexity: O(n) for the dictionary. 
# Dictionaries in Python are implemented as hash tables. Hash tables will have n keys and n elements (one for each key).

class Solution:
    def twoSum(self, nums, target):
        val_and_idx = {} # dictionary to store the number and its index
        # python documentation --> 5.6 
        # When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
        for index, value in enumerate(nums):
            if target - value in val_and_idx:
                return [val_and_idx[target - value], index]
            val_and_idx[value] = index
        return None
