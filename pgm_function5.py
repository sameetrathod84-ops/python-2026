#palindrome check
def palindrome(n):
    temp=n
    rev=0
    while n> 0:
        rev=rev*10 + n%10
        n//=10
    return'palindeome' if temp==rev else 'not palindrome'
print(palindrome(121))
