class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findleft(nums,target):         #for finding first position
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
        def findright(nums,target):               #for finding the last position
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
        if left_idx<=right_idx:                            #for checking whether first index less than or equal to right index
            return [left_idx,right_idx]                       #return leftindex,rightindex else return (-1,-1)
        return [-1,-1]           
    
                
