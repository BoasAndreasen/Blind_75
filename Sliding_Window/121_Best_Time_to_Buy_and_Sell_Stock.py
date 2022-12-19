class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        left_pointer = 0
        right_pointer = 1

        while right_pointer < len(prices):
            if prices[right_pointer] < prices[left_pointer]:
                left_pointer = right_pointer
            elif (prices[right_pointer] - prices[left_pointer]) > maximum:
                maximum = prices[right_pointer] - prices[left_pointer]
            right_pointer += 1
        return maximum
