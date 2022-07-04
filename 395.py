#recursion
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        
        def rec(st):
            ans=0
            if len(st)<1:
                return 0
            d=dict()
            #frequency count
            for i in st:
                if i in d:
                    d[i]+=1
                else:
                    d[i]=1
            start=0
            Fault=False
            for i in range(len(st)):
                if d[st[i]]<k:
                    ans=max(ans,rec(st[start:i]))
                    start=i+1
                    Fault=True
            if Fault:
                ans=max(ans,rec(st[start:]))
                return ans
            else:
                return len(st)

        return rec(s)




#queue or stack
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans=0
        q=[s]
        while(len(q)):
            word=q.pop(0)
            d=Counter(word)
            if len(word)<=ans:
                continue
            if min(d.values())>=k:
                ans=max(ans,len(word))
                continue
            start=0
            for i in range(len(word)):
                if d[word[i]]<k:
                    q.append(word[start:i])
                    start=i+1
            q.append(word[start:])

        return ans

