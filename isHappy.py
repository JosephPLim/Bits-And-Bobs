#Determines if a given number, n, is happy. Yes, this was a LeetCode assignment.
def isHappy(self, n):
  """
  :type n: int
  :rtype: bool
  """
  cycles = {}
  while n != 1:
    if n in cycles.keys(): return False
    temp = n
    curr = []
  while n != 0:
    digit = n % 10
    curr.append( digit * digit )
    n = n//10
            
  for i in range (0, len(curr)):
    n+= curr[i]
    cycles[temp] = n

  return True
