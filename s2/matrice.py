""" n = int(input("Nombre de lignes: "))

triangle = []

for i in range(n):
    if i == 0:
        triangle.append([1])
        #print (triangle)
    else:
        ligne = [1]
        for j in range(1, i):
           # print(triangle[i-1][j-1], triangle[i-1][j])
           #n=3
            ligne.append(triangle[i-1][j-1]+ triangle[i-1][j])

        ligne.append(1)
        triangle.append(ligne)
        

for ligne in triangle:
    print(ligne)
 """

n = int(input("Nombre de lignes: "))
for i in range(n):
    x=1

    for j in range(i+1):
        print(x,end=" ")
        x=x*(i-j)//(j+1)
print()

