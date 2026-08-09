class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # val ->  idx

        for i, n in enumerate(nums):
            # print(i," ",n)
            d = target - n
            if d in mapping:
                return [mapping[d], i]
            mapping[n] = i

        