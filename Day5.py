# jump game

class Solution(object):
    def canJump(self, nums):
        if len(nums) <= 1:
            return True

        max_reach = nums[0]

        for i in range(len(nums)):
            if i > max_reach:
                return False

            max_reach = max(max_reach, i + nums[i])

            if max_reach >= len(nums) - 1:
                return True

        return False

# Test cases
nums1 = [2, 3, 1, 1, 4]
nums2 = [3, 2, 1, 0, 4]

solution = Solution()
result1 = solution.canJump(nums1)
result2 = solution.canJump(nums2)

print(result1) 
print(result2)  
