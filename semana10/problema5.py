list=[]
while True:
    num = int(input("Ingrese un numero: "))
    if num <= 0:
        break
    list.append(num)
list.sort()
list.reverse()
print(sorted(list, reverse=True))

