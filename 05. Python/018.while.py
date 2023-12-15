contador = 0
while contador < 10:
    print(f'contador:{contador}')
    contador += 1
    
print('fin')

precios = [5.99, 10.99, 4.32, 8.76]
contador = 0

while contador <len(precios):
    precios[contador] *=0.80 #descuento 20%
    precios +=1
    
print(precios)
