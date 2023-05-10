dp={}
def fibo(n):
    if(n <= 2):
        return n
    else:
        if(n in dp):
            return dp[n]
        else:
            dp[n]= fibo(n-1)+fibo(n-2)
            return dp[n]

print(fibo(100))
