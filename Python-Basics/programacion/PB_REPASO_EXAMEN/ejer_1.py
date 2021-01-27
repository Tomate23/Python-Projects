"""
1. Escriu un programa que demani un text, i a continuació digui el número de
lletres “a” que conté. Per exemple, la paraula “patata” conté tres “a”.
"""
txt=str(input("introduce una palabra:\n"))
num_a=1
for x in txt:
    if x=="a":
        print(f"hay {num_a} letras [a]")
        num_a+=1
        
        

    