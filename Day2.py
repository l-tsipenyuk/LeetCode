#remove duplicates from unsorted array

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = list(set(nums))
        return f"{len(k)}, nums = {k}"
# alternative:
        # nums[:] = sorted(set(nums))
        # return nums



# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]

solution = Solution()
result = solution.removeDuplicates(nums)
print(result)