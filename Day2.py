#remove duplicates from unsorted array

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         k = list(set(nums))
#         return f"{len(k)}, nums = {k}"
# # alternative:
#         # nums[:] = sorted(set(nums))
#         # return nums



# # nums = [1,1,2]
# nums = [0,0,1,1,1,2,2,3,3,4]

# solution = Solution()
# result = solution.removeDuplicates(nums)
# print(result)


#remove duplicates from unsorted array = part II

# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """

#         k = []
#         i = 0

#         while i<len(nums):
#             count = 0
#             while i+count < len(nums) and nums[i] == nums[i + count]:
#                 count += 1

#             if count == 1:
#                 k.append(nums[i])
#             elif count > 1:
#                 k.extend([nums[i]]*2)

#             i += count
            
#         return k


# nums = [1,1,1,2,2,3]      
# solution = Solution()
# result = solution.removeDuplicates(nums)
# print(result)







