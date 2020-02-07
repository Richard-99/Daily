class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    return [arr.index(target), len(arr) - 1 - arr[::-1].index(target)]
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]

