s = "AABABBA"
# s = "ABAB"
k = 1
def func(s,k):
    i=0
    j=1
    n=len(s)
    l=k
    maxm=0

    while(i<=j and j<n):
        if(s[i]==s[j]):
            j+=1
        elif(s[i]!=s[j] and l>0):
            j+=1
            l-=1
        else:
            maxm=max(maxm,j-i)
            i+=1
            j=i+1
            l=k
    maxm=max(maxm,j-i)
    return maxm

print(func(s,k))
            


