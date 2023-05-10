def isPal(s,i,j):
    while(i<=j):

        if(s[i]!=s[j]):
            return False
        i+=1
        j-=1
    return True
            
def palindrome(s,i,j):
    if(i>j):
        return ''
    else:
        if(isPal(s,i,j)):
            stri=s[slice(i,j+1)]
            print(stri)
            return stri
        else:
            left=palindrome(s,i+1,j)
            right=palindrome(s,i,j-1)
            if(len(left)>len(right)):
                return left
            else:
                return right
s="babad"
print(palindrome(s,0,len(s)-1))