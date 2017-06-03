import itertools

def second_largest(numbers):
    count = 0
    m1 = m2 = float('-inf')
    for x in numbers:
        count += 1
        if x > m2:
            if x >= m1:
                m1, m2 = x, m1            
            else:
                m2 = x
    return m2 if count >= 2 else None

n = int(input())
j = input().split()
li=[]
for i in j:
    li.append(int(i))
com=[]
for s in range(n):
    com1= itertools.combinations(li,s)
    for i in com1:
        com.append(list(i))
count = 0
for i in com:
#    print(i)
    if len(i)!=0 and len(i)!=1:
        ll = i.index(max(i))
        sll = second_largest(i)
        if sll!=None:
            sl = i.index(second_largest(i))
            if sl < ll:
                count = count+1
                print(i)
print(count)
