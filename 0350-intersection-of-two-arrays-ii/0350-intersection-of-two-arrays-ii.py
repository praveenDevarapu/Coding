from collections import Counter
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a=Counter(nums1)
        b=Counter(nums2)
        dic=[]
        for i,freq in a.items():
            if i in b:
                dic+=[i]*min(freq,b[i])
        return dic