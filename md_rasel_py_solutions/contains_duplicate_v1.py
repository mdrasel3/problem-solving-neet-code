"""
Created on Dec 16 20:45:02 2024
@Author: Md. Rasel
"""
# Problem Statement: Given an array of integers `nums` return `true` if any value appears
# more than once in the array, otherwise return `false`

# Soln approarch: If every number is unique then the set length is same as
# the list length (return false). If this is not true, then there are duplicates.
# Time complexity: O(n)
# Space complexity: O(n) for the set.

class Solution:
    def hasDuplicate(self, nums):
        # typecasing the list to set
        myset = set(nums)
        if len(myset) == len(nums):
            return False
        else:
            return True