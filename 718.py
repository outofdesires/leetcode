#sliding window
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        def find(subarr) -> bool :
            for i in range(0,len(nums2)-len(subarr)+1):
                if nums2[i]==subarr[0]:
                    if subarr==nums2[i:i+len(subarr)]:
                        return True
            return False
        ans=0
        tsubarr=[]
        for i in nums1:
            tsubarr.append(i)
            if find(tsubarr):
                ans=max(ans,len(tsubarr))
            else:
                tsubarr=tsubarr[1:]

        return ans
#DP
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0]*(len(nums1)+1) for i in range(len(nums2)+1)]
        ans=0

        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums1[j-1]==nums2[i-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                    ans=max(ans,dp[i][j])
        return ans