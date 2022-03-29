<a href = "https://leetcode.com/contest/weekly-contest-286/problems/find-the-difference-of-two-arrays/"> Link of the problem </a>
<h3> Code : </h3>
class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        Dict1 = {}
        Dict2 = {}
        for val in nums1 :
            if val in Dict1 :
                Dict1[val] += 1
            else :
                Dict1[val] = 1
        
        for val in nums2 :
            if val in Dict2 :
                Dict2[val] += 1
            else :
                Dict2[val] = 1
        
        List = []
        temp = []
        for val in nums1 :
            if val not in Dict2 and val not in temp:
                temp.append(val)
        List.append(temp)
        temp1 = []
        for val in nums2 :
            if val not in Dict1 and val not in temp1:
                temp1.append(val)
        List.append(temp1)
        return List
