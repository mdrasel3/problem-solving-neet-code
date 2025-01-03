class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = 0
        for i in range(0,len(nums)-1,1):
            for j in range(i+1,len(nums),1):
                if nums[i] == nums[j]:
                    count+=1
        if count == 0:
          return False
        else:
          return True
             