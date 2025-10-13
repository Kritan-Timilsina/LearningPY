class Solution:
    def print_even_indices(self, s: str):
        #code here
        for i in range(len(s)):
            if i%2==0:
                print (s[i],end="") 