def isPalindrome(s):
    return s == s[::-1]
s=input()
res=isPalindrome(s)
if res:
    print("YES")
else:
    print("NO")    
