#User function Template for python3


class Solution:
    def nextLargerElement(self,nums,n):
           
        v = []
        st = []
        for i in range(len(nums)-1,-1,-1):
            if len(st)==0:
                v.append(-1)
            elif len(st)>0 and st[-1]>nums[i]:
                v.append(st[-1])
            elif len(st)>0 and st[-1]<=nums[i]:
                while len(st)>0 and st[-1] <= nums[i]:
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
import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        obj = Solution()
        res = obj.nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends