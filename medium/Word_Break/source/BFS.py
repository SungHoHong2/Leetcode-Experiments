class Solution(object):
    def wordBreak(self, s, wordDict):
        # convert the wordDict to set
        wordSet = set(wordDict)
        # set up a queue to search all the substrings
        queue = list()
        # set the record of visited for the substrings
        visited = [False for i in range(len(s))]
        # append the queue with the starting point zero
        queue.append(0)
        # loop until the queue is depleted
        while queue:
            # pop the next begining index of the substring
            start = queue.pop()
            # if the substring is not visited
            if not visited[start]:
                # iterate the substring
                for end in range(start+1,len(s)+1):
                    # if the substring is part of the wordset
                    if s[start:end] in wordSet:
                        # append the the end index to the queue
                        queue.append(end)
                        # if end index reached the final index of the string
                        if end == len(s):
                            # return true
                            return True
                # record the substring as visited
                visited[start] = True
        # return false if there are no branches that will create all valid substrings
        return False