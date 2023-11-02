class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        m,count=set(nums),1
        while count in m:
            count+=1
        return count
        