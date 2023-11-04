from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=Counter(nums1)
        b=Counter(nums2)
        l=[]
        for i,freq in a.items():
            if i in b:
                l+=[i]*min(freq,b[i])
        return l