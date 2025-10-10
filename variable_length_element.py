def sum(init_sum,*elements):# it creates tuples 
    res=init_sum
    for x in elements:
        res=res+x
    return res
print(sum(2,20))
print()
print(sum(20,30,40))
print()
print(sum(1,2,3,4,5,6,7,8))