class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        

        stack = []
        next_greater = {}

        for num in nums2:
            while stack and num > stack[-1]:
                previous = stack.pop()
                next_greater[previous] = num

            stack.append(num)

        for num in stack:
            next_greater[num] = -1

        answer = []

        for num in nums1:
            answer.append(next_greater[num])

        return answer