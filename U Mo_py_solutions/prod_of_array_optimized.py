def productExceptSelf(self, nums: List[int]) -> List[int]:
    # author Umo
    result = [0] * len(nums)
    # for storing prefix
    left = [0] * len(nums)
    # for storing suffix
    right = [0] * len(nums)

    left[0] = right[len(nums) - 1] = 1
    # using dp concept for storing mult data
    for i in range(1, len(nums)):
        left[i] = nums[i - 1] * left[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        right[i] = nums[i + 1] * right[i + 1]

    for i in range(len(nums)):
        result[i] = left[i] * right[i]
    
    return result
