nombre=['Luis','Yerly','Vanessa','Laura']
while True:
    numero = int(input("Numero: "))
    if numero <= 0:
        print("El numero debe ser mayor a 0")
        break
    print(nombre[numero - 1]) 
