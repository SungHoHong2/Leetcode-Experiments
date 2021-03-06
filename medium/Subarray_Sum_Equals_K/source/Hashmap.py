class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # initialize a hashmap
        hashmap = collections.defaultdict(int)
        # set the variables for counter and the sum
        count, sum = 0, 0
        # count the number of contiguous subsets that sum up to zero
        hashmap[0] = 1
        # iterate the numbers
        for i in nums:
            # expand the size of the contiguous subset
            sum += i
            # aggregate the number of subsets that can be equal to k
            count += hashmap[sum-k]
            # record the number of the contiguous subsets that equals to a certain number
            hashmap[sum] += 1
        # return the number of counts
        return count