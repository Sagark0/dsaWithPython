def Reduced_String(k, s):
        st=[]
        count=0
        for i in range(len(s)):
            if(len(st)<=0):
                st.append((s[i],1))
            else:
                (ch,count)=st[-1]
                if(ch==s[i]):
                    count+=1
                    st.append((s[i],count))
                    if(count==k):
                        while(count>1):
                            (ch,count)=st[-1]
                            st.pop()
                        
                else:
                    st.append((s[i],1))

        print(st)
        return 'ab'
s = "geegsforgeeeks"
k=2
print(Reduced_String(k,s))