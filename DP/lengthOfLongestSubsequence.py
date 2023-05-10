s1='abaadc'
s2='acbacdc'

def func(s1,s2,i,j,dp):
    if(i<0 or j<0):
        return 0
    elif(s1[i]==s2[j]):
        return func(s1,s2,i-1,j-1,dp)+1
    else:
        if((i,j) not in dp):
            str1=func(s1,s2,i,j-1,dp)
            str2=func(s1,s2,i-1,j,dp)
            dp[(i,j)]=max(str1,str2)
        return dp[(i,j)]

print(func(s1,s2,len(s1)-1,len(s2)-1,{}))