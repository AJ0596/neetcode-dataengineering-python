class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashDup = set()
        for i in nums:
            if i in hashDup:
                return True
            hashDup.add(i)
        return False
        