# W words in string
# Program swaps Word 1 with Word W, Word 2 with Word W-1 ...

tc = int(raw_input())  # The number of testcases
j = 0
str3 = []
while j < tc:
    str1 = raw_input()
    str2 = ""
    len1 = len(str1)
    list1 = []
    i = 0  # The perpetual iterator
    k = 0
    if len1 < 100000:
        while i < len1:
            if str1[i] == ' ' or i==len1-1:
                list1.append(str1[k:i+1])
                k=i+1
            i += 1
    # print list1
    lenlist = len(list1)
    s = 0
    t = lenlist-1
    if lenlist % 2 == 0:
        while s < t:
            list1[s], list1[t] = list1[t], list1[s]
            s = s+1
            t = t-1
    else:
        while(s!=t):
            list1[s],list1[t]=list1[t],list1[s]
            s=s+1
            t=t-1
    for jj in list1:
        str2=str2+" "+jj
    str3.append(" ".join(str2.split()))
    j=j+1
k=0
while k < j:
    print str3[k]
    k=k+1
