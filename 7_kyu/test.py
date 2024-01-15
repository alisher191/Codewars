# def twoSum(nums, target):
#     d = {}
#     for i, j in enumerate(nums):
#         r = target - j
#         if r in d:
#             return [d[r], i]
#         d[j] = i

# print(twoSum([2,7,11,15,3], 10))
# 121. Best Time to Buy and Sell Stock | Leetcode
def maxProfit(prices):
    for i, v in enumerate(prices):
        if min(prices[i:]) < v:
            continue
        elif max(prices[i:]) > v:
            return max(prices[i:]) - v
    return 0
print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([2,4,1]))
print(maxProfit([3,2,1]))
print(maxProfit([2,1,4]))
