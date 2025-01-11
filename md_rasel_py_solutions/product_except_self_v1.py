# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 21:48:52 2025

@author: Md Rasel
"""
# Problem Statement: Given an integer array `nums`, return an array `output` 
# where `output[i]` is the product of all the elements of `nums` except `nums[i]`

# Soln approach: find ther prod of all elements except if it is a zero
# if element is 0, increment count, iterate through array again
# if the count of 0 is greater than 2, product of all numbers will be 0
# if only one 0, then all other elements product will be 0,
# but for that 0 entry: output array will be equal to product of the array
# if no zeros are found then product of each element is product divided by itself
# Time complexity: O(n) 
# Space complexity:

class Solution:
    def productExceptSelf(self, nums):
        # count if there is any zero in the array
        zero_count = 0
        n = len(nums)
        product = 1
        # initialization of output array
        result = [0] * n

        # if the element is 0 increment the count
        for num in nums:
            if num == 0:
                zero_count += 1
            # if not calculate product of all elements
            else:
                product *= num
        
        for i in range(n):
            # if the count of 0 is greater than 2, product of all numbers will be 0
            if zero_count > 1 :
                result[i] = 0
            # if only one 0, then all other elements product will be 0,
            # but for that 0 entry: output array will be equal to product of the array
            elif zero_count == 1:
                if nums[i] == 0:
                    result[i] = product
                else:
                    result[i] = 0
            # if no zeros are found then product of each element is product divided by itself
            else:
                result[i] = product // nums[i]   
        return result
        