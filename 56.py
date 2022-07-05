class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack=[]
        intervals.sort(key= lambda x : x[0])
        stack.append(intervals[0])
        for i in range(1,len(intervals)):

            if intervals[i][0] <= stack[-1][1]:
                
                a=stack.pop(-1)
                stack.append([a[0],max(a[1],intervals[i][1])])
            else:
                stack.append(intervals[i])
        return stack