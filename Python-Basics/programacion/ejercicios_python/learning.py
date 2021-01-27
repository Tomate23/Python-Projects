"""
lista=["pedro","ramon","maria","alba","sandra"]
num_items=len(lista)
print("the number of items in this list are:%s" % num_items)
if num_items <=5:
    print("there are at least 5 items inside this list")
print("showing the items...")
for x in lista:
    print(x)
print("would you like to change any item of this list")
aw=str(input("say 'yes' or 'not': \n"))
if aw == "yes":
    print("which one would you like to chage? \t 'pedro','ramon','maria','alba','sandra'")
    ch=str(input("answer: \n"))
    if ch == "ramon":
        print("instead what item would you like to change?")
        newit=str(input("insert the new item: \n"))
        lista[1]= newit
        print(lista)
else:
    print("if you don't want to do any change, see ya")
"""
lista1=["osmar","josue","vallecillo"]
del lista1
print(lista1)



    