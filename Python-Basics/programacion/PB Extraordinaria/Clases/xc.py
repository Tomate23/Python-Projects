cad1 = input("introduce frase")
cad2 = ''
for i in cad1:
    if i == 'A':
        cad2 += '4'
    if i == 'E':
        cad2 += '3'
    if i == 'I':
        cad2 += '1'
    if i == 'O':
        cad2 += '0'
    else:
        cad2+=i
print(cad1)
print(cad2)
        