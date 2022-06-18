for _ in range(int(input())):
    n,m,k=map(int,input().split())
    a=input()
    b=input()
    s1=sorted(a)
    s2=sorted(b)
    c=''
    ak=k
    bk=k
    i=0
    j=0
    while(i<n and j<m):
        if(s1[i]<=s2[j] and ak>0 or bk<=0):
            c+=s1[i]
            i+=1
            ak-=1
            bk=k
        elif(bk>0):
            c+=s2[j]
            j+=1
            bk-=1
            ak=k
    print(c) 
    
