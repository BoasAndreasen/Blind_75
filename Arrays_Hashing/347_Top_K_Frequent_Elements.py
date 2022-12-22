import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        sort dictionary with letter frequency and take k keys
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return [x[0] for x in sorted(collections.Counter(nums).items(), key=lambda x: x[1], reverse=True)][:k]
