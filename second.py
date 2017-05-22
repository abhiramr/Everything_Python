nn = int(raw_input())
res = []
for i in range(nn):
    nk = raw_input()
    nkk = [(x) for x in nk.split()]
    #print nkk
    n = int(nkk[0])
    k = int(nkk[1])
    li =[]
    for i in range(n):
        s = raw_input()
        li.append([(x) for x in s.split()])
    j = []
    #print li
    for i in li:
        i.pop(0)
        j = j+i
    liUni = list(set(j))
    #print "unique=",str(liUni)

    if len(liUni) < k:
        res.append("sad")
    else:
        only1=[]
        for s in j:
            if j.count(s) == 1:
                only1.append(s)
               # print s 
#            print li.index(s)
        yes = 0
        for i in li:
                if len(i) == k:
                    yes = 0
                    break
                b3 = [val for val in only1 if val in i]
                if len(b3) == 1:
                    yes = 1
                    break
        if yes ==1:
            res.append("all")
        else:
            res.append("some")
for i in res:
    print i
