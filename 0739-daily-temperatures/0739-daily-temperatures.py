class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        ans = [0] * len(temperatures)  #if we never find warmer day, ans will be 0

        stack = [] #stores indexes of days waiting for warmth
        
        for i in range(len(temperatures)):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous = stack.pop() #if current day is warmer, pop waiting day
                ans[previous] = i - previous
                
            stack.append(i)
        
        return ans


      