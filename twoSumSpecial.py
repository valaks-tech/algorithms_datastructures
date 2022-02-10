#
# nums Array is not sorted
# Two Sum and dups may present
# ********************************
import collections

class Solution:
    def twoSumSpecial(nums, target):
        hash_map = collections.Counter(nums)

        for num in hash_map.keys():
            complement = target - num

            if complement != num:
                if complement in hash_map:
                    return complement , num
            elif hash_map[num] > 1:
                return complement, num   # well its dups in this case!
        
        return -1, -1

target = 16
nums = [1,5,8,9,3,8]
print(Solution.twoSumSpecial(nums,target))
