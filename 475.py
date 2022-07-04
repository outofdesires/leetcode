class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        def find(house):
            #binary search mod
            i=0
            j=len(heaters)-1
            while(i<j):
                mid=(i+j)//2
                if heaters[mid]==house:
                    return 0
                if house<heaters[mid]:
                    j=mid
                else:
                    i=mid+1
            if i==0:
                return abs(heaters[i]-house)
            return min(abs(heaters[i]-house),abs(heaters[i-1]-house))
        rangeh=0
        for house in houses:
            rangeh=max(rangeh,find(house))
        return rangeh


