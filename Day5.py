# # jump game

# class Solution(object):
#     def canJump(self, nums):
#         if len(nums) <= 1:
#             return True

#         max_reach = nums[0]

#         for i in range(len(nums)):
#             if i > max_reach:
#                 return False

#             max_reach = max(max_reach, i + nums[i])

#             if max_reach >= len(nums) - 1:
#                 return True

#         return False

# # Test cases
# nums1 = [2, 3, 1, 1, 4]
# nums2 = [3, 2, 1, 0, 4]

# solution = Solution()
# result1 = solution.canJump(nums1)
# result2 = solution.canJump(nums2)

# print(result1) 
# print(result2)  



# dataframe

import pandas as pd

def createDataframe(student_data):
    df = student_data
    res = pd.DataFrame(data = df, columns = ["student_id", "age"])
    return res



student_data = [
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]


result = createDataframe(student_data)
print(result)