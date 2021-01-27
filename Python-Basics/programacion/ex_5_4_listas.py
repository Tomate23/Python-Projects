"""
5.4 Crea un programa llamado ex_5_4 que almacene en un vector la nota de los alumnos de un
grupo de prácticas, y posteriormente calcule y visualice el número de notas que aparecen dentro
de los siguientes intervalos:
[0 , 5[ Insuficiente
[5 , 7[ Aprobado
[7 , 9[ Notable
[9 , 10] Excelente
Tened en cuenta que, aunque los grupos de prácticas tienen un máximo de treinta alumnos,
cada grupo puede tener un número de alumnos diferente. El programa debe funcionar para
cualquier grupo.
"""
st=int(input("insert the numbre of students you want evaluate:\n"))
marks=[]
for _ in range(st):
    mark=int(input("insert the marks of the students:\n"))
    marks.append(mark)
    if mark>=0 and mark<5:
        print(f"not enough mark: {mark}")
    elif mark>=5 and mark<7:
        print(f"you pass: {mark}")
    elif mark>=7 and mark<9:
        print(f"good mark:{mark}")
    elif mark==9 or mark==10:
        print(f"you btilliant dude: {mark}")
print(marks)
        
