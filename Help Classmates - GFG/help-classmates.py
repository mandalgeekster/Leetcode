#User function Template for python3

class Solution:
    def help_classmate(self, nums, n):
      
        v = []
        st = []
        for i in range(len(nums)-1,-1,-1):
            if len(st)==0:
                v.append(-1)
            elif len(st)>0 and st[-1]<nums[i]:
                v.append(st[-1])
            elif len(st)>0 and st[-1]>=nums[i]:
                while len(st)>0 and st[-1] >= nums[i]:
                    st.pop()
                if len(st)==0:
                    v.append(-1)
                else:
                    v.append(st[-1])
            st.append(nums[i])
        return v[::-1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [ int(x) for x in input().split() ]
        obj = Solution()
        result = obj.help_classmate(arr,n)
        for i in result:
            print(i,end=' ')
        print()

# } Driver Code Ends