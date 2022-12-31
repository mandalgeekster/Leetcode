class Solution:
    def nextGreaterElements(self, nums1: List[int]) -> List[int]:
        nums = nums1+nums1
        v = []
        st = []
        for i in range(len(nums)-1,-1,-1):
            if len(st)==0:
                v.append(-1)
            elif len(st)>0 and st[-1]>nums[i]:
                v.append(st[-1])
            elif len(st)>0 and st[-1]<= nums[i]:
                while len(st)>0 and st[-1] <= nums[i]:
                    st.pop()
                if len(st)==0:
                    v.append(-1)
                else:
                    v.append(st[-1])
            st.append(nums[i])
        ans = v[::-1]
        return ans[:len(nums1)]
        