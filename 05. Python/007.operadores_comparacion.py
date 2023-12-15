#todos los operadores devuelven booleaan True or False

# = es asignacion de un valor a una variable

# Igual == 

password = input ('Introduce constraseña:  ')
password_correct = 'admin'
print (password == password_correct)

email = input ('introduce to email')
email_correct = 'alan@gmail.com'
print (email == email_correct)

password = input('Introduce constraseña:  ')
password_correct = 'admin'
if password != password_correct:
     print("credenciales incorrectas")
else:
    print("credenciales correctas")
    
respuesta_correcta = 'madrid'
capital = input ('introduce capital de spain: ' ).lower().replace(" ","")

if capital !=respuesta_correcta:
    print('respuesta incorrecta. ')
else:
    print('has acertado toma una monedita.')
    
# >mayor que (Greater than, gt)
# >= mayor o igual que (Greater than or equals, GTE)
 
# >menor que (Less than, gt)
# >= mayor o igual que (Less than or equals, GTE)
 
print(50>20)    #True  
print(50>50)   #False
print(50>=20)    #True  
print(50>100)   #False


# <menor que (Less than, gt)
# <= mayor o igual que (Less than or equals, GTE)
print(50<20)    #True  
print(50<50)   #False
print(50<=20)    #True  
print(50<100)   #False

