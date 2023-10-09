#1. merge 2 lists

# class Solution(object):
#     def merge(self, nums1, m, nums2, n):
#         """
#         :type nums1: List[int]
#         :type m: int
#         :type nums2: List[int]
#         :type n: int
#         :rtype: None Do not return anything, modify nums1 in-place instead.
#         """
#         # nums1 = [1,2,3,0,0,0]
#         # m = 3 
#         # nums2 = [2,5,6]
#         # n = 3
#         for i in range(0, len(nums2)):
#             nums1.append(nums2[i])
#             nums1.remove(0)
#             nums1.sort()
#         return nums1

# # nums1 = [1,2,3,0,0,0]
# # m = 3 
# # nums2 = [2,5,6]
# # n = 3

# solution = Solution()
# result = solution.merge(nums1, m, nums2, n)
# print(result)


#remove element 

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = []
        a = nums.count(val)

        for i in nums:
            if i != val:
                k.append(i)

        for _ in range(a):
            k.append("_")

        return f"{a}, nums = {k}"

# alternative:
#         while val in nums:
#             nums.remove(val)




nums = [3,2,2,3]
val = 3

solution = Solution()
result = solution.removeElement(nums, val)
print(result)