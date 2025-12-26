class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)      # don't increment i; next item shifts into i
            else:
                i += 1
        return len(nums)


        