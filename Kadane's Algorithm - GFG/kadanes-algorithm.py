#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        pr = -10**7+2-1
        maxi = 0
        for i in range(len(arr)):
            maxi = arr[i]+maxi 
            if pr <maxi:
                pr = maxi 
            if maxi < 0:
                maxi  = 0
        return pr
         
        ##Your code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends