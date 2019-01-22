class Solution(object):
   """
   type nums: List[int]
   type target: int
   rtype: List[int]
   """
  def twosum(self,nums,target):
      dict = {}
      for i in range(0,len(nums)):
          complement = target - nums[i]
          if dict.get(complement) is not None:
              return [dict[i],i]
          dict[nums[i]] = i 