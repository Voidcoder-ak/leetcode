class Solution(object):
    def twoSum(self, nums, target):
        
        x = len(nums)

        for i in range(0, x):
            for j in range(i+1, x):
                if nums[i] + nums[j] == target:
                    return [i,j]