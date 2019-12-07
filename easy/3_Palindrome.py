from typing import List, Dict

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)

        if x < 0:
            return False

        if strnum == strnum[::-1]:
            return True
        else:
            return False

def main():
    print(Solution().isPalindrome(121))

if __name__ == "__main__":
    main()
