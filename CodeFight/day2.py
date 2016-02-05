a = [0,2]
b = [5,1]

mat = [[4,5,3,-4,3,8], 
 [2,0,6,5,4,9], 
 [7,5,6,8,2,6], 
 [1,4,7,8,9,11], 
 [1,3,10,5,5,1], 
 [12,7,3,4,4,3]]
x = dict()

for elem in mat:
    for j in elem:
        x[j] = x[j]+ x.get(j,1)

#if zero exist

#if middle number exist

#if middle number is missing 


