n = "7970521.5544"
nw = ""
nd = ""

for i in range(len(n)):
    if n[i] == ".":
        nw = n[0:i]
        nd = n[i+1:len(n)]

x = list()
y = list()

for i in range(len(nw)+1):
    x.append(int(nw) % 10**(i+1))

x[1] = 0
for j in range(len(x)-1):
     y.append(x[j+1] - x[j])


        

    
