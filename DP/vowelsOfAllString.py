word = "ab"


def checkVowels(word,start,i):
    count=0
    vowels=['a','e','i','o','u']
    for i in range(start,i+1):
        if(word[i] in vowels):
            count+=1
    return count

def count(word,dp,start,end):
    if(start>end):
        return 0
    else:
        sum=0
        if((start,end) not in dp):
            for i in range(start,end+1):
                sum+=checkVowels(word,start,i)
            dp[(start,end)]=count(word,dp,start+1,end)+sum
        return dp[(start,end)]

print(count(word,{},0,len(word)-1))