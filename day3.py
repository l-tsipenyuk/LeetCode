#  Majority Element
# class Solution(object):
#     def majorityElement(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
        
#         for i in nums:
#             if nums.count(i) > len(nums)/2:
#                 return i


# nums = [3,2,3]
# solution = Solution()
# result = solution.majorityElement(nums)
# print(result)


# Rotate array

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return  
        
        n = len(nums)
        k = k % n  
        
        if k == 0 or n == 1:
            return nums
        
        nums[:] = nums[-k:] + nums[:-k] 
        return nums 

# Test cases
nums1 = [1, 2, 3, 4, 5, 6, 7]
k1 = 3
# expected output [5, 6, 7, 1, 2, 3, 4]

nums2 = [-1, -100, 3, 99]
k2 = 2
# expected output [3, 99, -1, -100]

nums3 = [1]
k3 = 1
# expected output [1]

nums4 = [1, 2, 3]
k4 = 1
# expected output [3, 1, 2]

solution = Solution()
result1 = solution.rotate(nums1, k1)
result2 = solution.rotate(nums2, k2)
result3 = solution.rotate(nums3, k3)
result4 = solution.rotate(nums4, k4)

print(result1)
print(result2)
print(result3)
print(result4)



