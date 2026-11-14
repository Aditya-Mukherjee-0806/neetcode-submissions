class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * (n - 1)
        suffix = [0] * (n - 1)
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n - 1):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 3, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        output = [0] * n
        output[0] = suffix[0]
        output[-1] = prefix[-1]
        for i in range(1, n - 1):
            output[i] = prefix[i - 1] * suffix[i]
        return output