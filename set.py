"""List has distinct elements, they are unordred, no indexing , (union, intersection, set difference etc are fast ), use hashing internally"""
s={10,20,30}
print(type(s),s)
s2=set([20,30,40])
print(type(s2),s2)
s3={
    #it doesnot create empty set it creates empty dictionary 

}
print(type(s3))

s4=set()
print(type(s4))
print (s4)
s.add(4)
print(s)
#s.remove(1) yo remove chai cha bhani kaam garcha chaina bhani gardaina yesto ma discard chalauni telley problem lyaudaina 
s.discard (1)
print (len(s))
print(20 in s)
s1={
    2,4,5,6
}
s2={2,6,7,5,7,8}
print(s1|s2)# this symbol gives union of set 
print(s1&s2)# this gives intersection i.e. common element
print(s1-s2)#gives difference element present in s1 but not in s2 
print(s1^s2) # gives everything except common 
s3={2,4,6,8}
s4={4,8,12}
print(s3.isdisjoint(s4))
print(s3<=s4)# is subset 
print(s3<s4)#is proper subset
print(s3>=s4)#is superset
print(s3>s4)#proper superset