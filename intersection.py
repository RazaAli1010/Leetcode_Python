class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sett=set()
        result=[]
        for value in nums1:
            sett.add(value)
        for value in nums2:
            while value in sett:
                sett.remove(value)
                result.append(value)
        return result
