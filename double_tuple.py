def doubleTup(numbers):
    #code here
    l=list(numbers)
    for i in range(len(l)):
         l[i]=l[i]*2
    double=tuple(l)
    return double