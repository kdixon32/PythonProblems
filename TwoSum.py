# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(self, nums, target):
    pastval = dict()

    for i, elem in enumerate(nums):
        comp = target - elem
        if comp in pasval:
            return [pasval[comp], i]
        pastval[elem] = i
    return []