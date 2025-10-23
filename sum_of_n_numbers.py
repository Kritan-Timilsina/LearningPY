def nSum(n):
    #code here
    ans = 0
    for i in range (n,0,-1):
        ans+=i
    return ans
print(nSum(5))