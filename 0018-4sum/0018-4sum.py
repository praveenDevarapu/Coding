class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n-3):
            # avoid the duplicates while moving i
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i+1, n-2):
                # avoid the duplicates while moving j
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                l = j + 1
                r = n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res += [nums[i], nums[j], nums[l], nums[r]],

                        # skip duplicates
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        r -= 1
        return res