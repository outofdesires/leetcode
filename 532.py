#Binary search approach
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        def bs(arr,target) -> bool:
            i=0
            j=len(arr)-1
            while(i<=j):
                mid=(i+j)//2
                if arr[mid]==target:
                    return True
                if arr[mid]>target:
                    j=mid-1
                else:
                    i=mid+1
            return False
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            if bs(nums[i+1:],nums[i]+k):
                ans.add(nums[i])
        return len(ans)

#Hashmap
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d=dict()
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        ans=0
        for i in set(nums):
            if k==0:
                if d[i]>1:
                    ans+=1
            elif (i-k) in d:
                ans+=1
        return ans



