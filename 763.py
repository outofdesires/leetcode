class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lstidx=dict()
        for idx,i in enumerate(s):
            lstidx[i]=idx

        i=0
        ans=[]
        pv=0
        while(i<len(s)):
            bound=lstidx[s[i]]
            while(i<=bound):
                bound=max(bound,lstidx[s[i]])
                i+=1
            ans.append(i-pv)
            pv=i
        return ans
