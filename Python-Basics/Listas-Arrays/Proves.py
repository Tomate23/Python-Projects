'''
# Print a list reverse
a = [1,2,3,4,5]
ra = []
#print(len(a), end="\n")

#for i in range(len(a)):
#    ra.append(a[len(a)-i-1])

for i in range (len(a)-1,-1,-1): # como el -1 es el ultimo este no está incluido.
    ra.append(a[i])

print(ra)
'''
