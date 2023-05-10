# No of ways you can go to n steps taking 1 or 2 step at a time

def nSteps(n):
    if(n==1 or n==2):
        return n-1
    else:
        return nSteps(n-1)+nSteps(n-2)

print(nSteps(4))