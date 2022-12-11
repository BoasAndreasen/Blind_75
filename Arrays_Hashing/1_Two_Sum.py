class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}

        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            if (target - nums[i]) in d and i != d[target - nums[i]]:
                return [d[(target - nums[i])], i]