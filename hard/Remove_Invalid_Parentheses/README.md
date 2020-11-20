### Remove Invalid Parentheses
**Backtracking**
- [Source code](source/Backtrack.py)
```python
class Solution(object):

    def __init__(self):
        self.valid_expressions = None
        self.min_removed = None

    def reset(self):
        self.valid_expressions = set()
        self.min_removed = float("inf")

    """
        string: The original string we are recursing on.
        index: current index in the original string.
        left_count: number of left parentheses till now.
        right_count: number of right parentheses till now.
        expr: the resulting expression in this particular recursion.
        rem_count: number of parentheses ignored in this particular recursion.
    """
    def remaining(self, string, index, left_count, right_count, expr, rem_count):
        # reached the end of string.
            # if the expression is valid along wit the minimum removal
                # reset the return array if new minimum number is found
                # append the string to the return array
        # exploring the string
            # recurse one step ahead if the current character is not a parenthesis
            # if the current character is a parenthesis
                # removing one parenthesis
                # increment left and move forward if the current parenthesis is an opening bracket
                # increment right and move forward if the current parenthesis is a closing bracket
        pass

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Reset the class level variables that we use for every test case.
        # Recursive call
        pass
```

**Limited Backtracking**
- [Source code](source/Optimized.py)
```python
class Solution:
    def removeInvalidParentheses(self, s):

        # Find out the number of misplaced left and right parenthesis.
            # record the number of left parenthesis
            # record the number of right parenthesis
                # increment the number of misplaced right if left is zero
                # decrement the number of misplaced left

        def recurse(s, index, left_count, right_count, left_rem, right_rem, expr):
            # if the recursion reached the leaf
                # if the expression is valid
                    # add the answer
            # if the recursion is on progress
                # remove parenthesis only if the misplaced parenthesis exists
                    # remove parenthesis for left or right
                # if the current characetr is not a parenthesis
                # if left parenthesis
                # if right parenthesis and there are more left than right
            pass

        # Run the recursion tree and return the available answers
        pass
```