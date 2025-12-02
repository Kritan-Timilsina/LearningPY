n=input("Enter the number:")
def binToDec(n):
    res=0
    p=1
    for x in reversed (n):
        res=res+int(x)*p
        p=p*2
    return res
r=binToDec(n)
print(r)

"""
res=int(b,2)

#User function Template for python3

class Solution:
	def binaryToDecimal(self, b):
		# Code here
		res=0
		p=1
		for x in reversed(b):
		    res=res+int(x)*p
		    p=p*2
		return res
	
"""