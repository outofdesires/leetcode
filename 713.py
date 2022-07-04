class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i=0
        st=0
        totalprod=1
        if k<=1:
            return 0
        subarraycount=0
        while(i<len(nums)):
            totalprod*=nums[i]
            while(totalprod>=k):
                totalprod/=nums[st]
                st+=1
            subarraycount+=i-st+1
            i+=1
        return subarraycount