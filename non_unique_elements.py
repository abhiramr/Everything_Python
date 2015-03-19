
# Given a list of elements, find the elements that are non-unique

a = raw_input("Enter list of elements separated by space: ")
arr_a = a.split(' ')
non_unique = []
if arr_a == []:
    print("List is empty")
    exit()
for i in arr_a: 
    if a.count(i) > 1 and i != ' ':
        non_unique.append(i)
print("List of non-unique elements =>")
print(set(non_unique))
