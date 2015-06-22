from openpyxl import load_workbook
wb=load_workbook(filename='/Users/aramesh/Desktop/walmart-ipq.xlsx')
sheet_range=wb['Sheet1']
for i in range(2,36):
    flag=0
    t=(str(sheet_range['E'+str(i)].value).split('/')[-2:-1])
    k=str(t).split('-')
    li=[]
    for j in k:
#        print("j=",j)
        if ('[' in j or j.isalpha() or ']' in j) and flag==0:
            pass
        else:
            li.append(j)
            flag=1
    if len(li)!=0:
        print li[-2:]
    print("\n")
