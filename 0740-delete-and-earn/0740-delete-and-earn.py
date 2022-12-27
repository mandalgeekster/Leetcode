class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        num_count = defaultdict(int)
        for num in nums:
            num_count[num] += 1
        prev = 0
        cur = num_count[1]
        for num in range(2, max_num + 1):
            prev, cur = cur, max(prev + num_count[num] * num, cur)
        return cur