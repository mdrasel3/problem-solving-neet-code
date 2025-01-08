class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(0, len(nums)):
            newnums = nums[:]
            newnums.pop(i)
            product = 1
            for num in newnums:
                product*=num
            products.append(product)
        return products
