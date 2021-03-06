class Job:
    def __init__(self, start, finish, profit):
        self.start = start
        self.finish = finish
        self.profit = profit


class Solution:
    def getNonConflicting(self, jobs, n):
        # search the job that ends earlier than the current job
        for i in reversed(range(n)):
            # return the index of the latest job that does not conflict with the current job
            if jobs[i].finish <= jobs[n].start:
                return i
                # return -1 if every job is conflicting
        return -1

    def topdown(self, jobs, j):
        # return 0 if the recursion requests for incompatible jobs
        if j == -1:
            return 0
            # return the current profit if the recursive tree reached the leaf
        if j == 0:
            return jobs[j].profit
        # if the result of the current job is not recorded
        if not self.dp[j]:
            # find the compatible job
            compatible = self.getNonConflicting(jobs, j)
            # record the maximum possible profit for the current job
            self.dp[j] = max(jobs[j].profit + self.topdown(jobs, compatible), self.topdown(jobs, j - 1))
        # return the maximum possible profit for the current job
        return self.dp[j]

    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        # initialize a list to store jobs
        jobs = list()
        # append all the jobs (start, finish, profit)
        for i in range(len(profit)):
            jobs.append(Job(startTime[i], endTime[i], profit[i]))
        # sort the jobs by finish time
        jobs.sort(key=lambda x: x.finish)
        # initialize a map that records the maximum profit for each jobs
        self.dp = [0 for _ in jobs]
        # run the recursvie tree from top to bottom
        return self.topdown(jobs, len(jobs) - 1)