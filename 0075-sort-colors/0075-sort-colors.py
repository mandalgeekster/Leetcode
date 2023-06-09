class Solution:
    def sortColors(self, list1: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(1, len(list1)): 
   
            a = list1[i] 
  
            j = i - 1 
           
            while j >= 0 and a < list1[j]: 
                list1[j + 1] = list1[j] 
                j -= 1 
                 
            list1[j + 1] = a 
             
       
            