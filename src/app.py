import sys
import os


def palindrome(s):
    # your code goes here
    if s == None:
        return False

    s = s.lower()

    strLength = len(s)
    for i in range(math.floor(s)):
        if s[i] != s[strLength - 1 - i]:
            return False
    return True

def solution(s):
    return palindrome(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argment required"))

    print(solution(sys.argv[1]))
