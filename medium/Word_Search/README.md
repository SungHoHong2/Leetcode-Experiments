### Word Search
**Backtracking**
- `backtracking` is a methodology where we mark the current path of exploration
- if the path does not lead to a solution, we then revert the change and try another path.
- [Source code](source/backtrack.py)
```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # set the table as the global pointer
        # iterate all possible cells in the board 
                # return true if the snake is found from the recursion 
        # return false if the snake is not found
        pass

    def backtrack(self, row, col, suffix):
        # return true if the snake is completed
        # return false if the index exceeds the board or the suffix does not match
        # mark the index as visited
        # traverse the neighboring elements
            # return true if the snake is found from the recursion
        # reset the table back to original state to allow other recursions to search
        # return false when no snake is found
        pass
```


