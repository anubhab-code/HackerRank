def isPalindrome(s):
    isPalindrome = True
    for i in range(int(len(s) / 2) + 1):
        isPalindrome = isPalindrome and s[i] == s[-1 - i]
    return isPalindrome

def palindromeIndex(s):
    if isPalindrome(s):
        return -1
    else:
        for i in range(len(s)):
            if s[i] != s[-1 - i]:
                if isPalindrome(s[:i] + s[i+1:]):
                    return i
                elif isPalindrome( s[:(len(s)-1-i)] + s[(len(s)-i):] ):
                    return len(s) - 1 - i
                else:
                     return 'Error 1 :('
        return 'Error 2 :('

T = int(input())

cases = []
for _ in range(T):
    cases.append(input())

for s in cases:
    print(palindromeIndex(s))