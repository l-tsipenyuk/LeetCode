# H-index

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()  
        n = len(citations)
        h = 0

        for i, citation in enumerate(citations):
            h_candidate = min(citation, n - i)  
            h = max(h, h_candidate) 

        return h

citations = [3,0,6,1,5]
solution = Solution()
res = solution.hIndex(citations)
print(res)


