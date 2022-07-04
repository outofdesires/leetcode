class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        st=0
        totalsum=0
        m=sys.maxsize
        while(i<len(nums)):
            totalsum+=nums[i]
            while(totalsum>=target):
                m=min(m,i-st+1)
                totalsum-=nums[st]
                st+=1
            i+=1
        return 0 if m==sys.maxsize else m

