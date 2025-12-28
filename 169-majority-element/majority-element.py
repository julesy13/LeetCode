class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numsdict = {}
        for x in nums:
            numsdict.setdefault(x , 0)
            numsdict[x] += 1

        return max(numsdict, key = numsdict.get)
        