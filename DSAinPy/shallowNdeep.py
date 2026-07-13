import copy

#Shallow Copy
Originnaal = [[1, 2], [3, 4]]
shallow = copy.copy(Originnaal)

shallow[0][0] = 100
print("Original: ", Originnaal)
print("Shallow: ", shallow)

print()


#Deep Copy
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 100

print("Original: ", original)
print("Deep Copy: ", deep)
