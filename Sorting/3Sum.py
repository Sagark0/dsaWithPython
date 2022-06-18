a=[-1,0,1,2,-1,-4]
def func(a):
    a.sort()
    n=len(a)
    result=[]
    for i in range(n-2):
        if(i>0 and a[i]==a[i-1]):
            continue
        start=i+1
        end=n-1
        while(start<end):
            sum=a[i]+a[start]+a[end]
            if(sum>0):
                end-=1
            elif(sum<0):
                start+=1
            else:
                print(i,start,end)
                result.append([a[i],a[start],a[end]])
                while(start+1<n and a[start+1]==a[start]):
                    start+=1
                while(end-1>0 and a[end-1]==a[end]):
                    end-=1
                start+=1
                end-=1

    print(result)
func(a)