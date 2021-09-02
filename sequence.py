#röðin er summa síðustu 3ja talna 
#ef n = 8, 1,2,3,6,11,20,37,68

n = int(input("Enter the length of the sequence: "))
x,y,z = 1,2,3

count = 0
#print(x)
#print(y)
#print(z)
while count <= n:
    print(x)
    x = x+y+z
    count += 1
    if count >= n:
        break
    print(y)
    y = x+y+z
    count += 1
    if count >= n:
        break
    print(z)
    z = x+y+z
    count += 1
    if count >= n:
        break
    