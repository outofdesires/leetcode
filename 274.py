class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        hindex=0
        for i in citations:
            hindex+=1
            if i <hindex:
                return hindex-1
        return hindex
