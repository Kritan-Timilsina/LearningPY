def sequence(tup):
    # code here 
    d=tup[1]-tup[0]
    next_terms=[tup[-1]+d*(i+1) for i in range(3)]
    return tup +tuple(next_terms)