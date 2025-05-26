# can you change the values inside a list which is contained in a set 
# ANS: no 

s = {8, 7, 12, "Harry", [1,2]}  #REASON1=> Lists cannot be included in sets

s[4][0] = 9  #even of lists could have been included in sets...changing values via indexing is not allowed
