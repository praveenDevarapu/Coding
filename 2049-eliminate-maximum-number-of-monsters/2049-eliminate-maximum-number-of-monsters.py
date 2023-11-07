class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        n=len(dist)
        for i in range(n):
            dist[i]=ceil(dist[i]/speed[i])
        dist.sort()
        count=0
        for j in range(n):
            if count>=dist[j]:
                return count
            count+=1
        return n

