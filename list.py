lst = ['Apple', 'Mango', 'Guava']

print ("Length",len(lst))
print ("First",lst[0])
print ("Length",lst[-1])

lst.append('Papaya')
print("Append",lst)

lst.remove('Guava')
print("Remove",lst)

lst.sort()
print("Sort",lst)

lst.pop(0)
print("Pop",lst)

lst.reverse()
print("Reverse",lst)

print("Multiplication",lst*3)

lst = lst[:3]
print("Sliced",lst)

lst.clear()
print("Updated List",lst)