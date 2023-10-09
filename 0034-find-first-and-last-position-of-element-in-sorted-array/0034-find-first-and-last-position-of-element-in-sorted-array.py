class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findleft(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    r=m-1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return l
        def findright(nums,target):
            l,r=0,len(nums)-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    l=m+1
            return r
        left_idx=findleft(nums,target)
        right_idx=findright(nums,target)
        if left_idx<=right_idx:
            return [left_idx,right_idx]
        return [-1,-1]           
    
                