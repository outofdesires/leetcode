#Hashmap
class Solution:
    def numSubarraysWithSum(self, nums: List[int], k: int) -> int:
        prefixsum=0
        d=dict()
        d[0]=1
        count=0
        for i in nums:
            prefixsum+=i
            if prefixsum-k in d:
                count+=d[prefixsum-k]
            if prefixsum in d:
                d[prefixsum]+=1
            else:
                d[prefixsum]=1
        return count