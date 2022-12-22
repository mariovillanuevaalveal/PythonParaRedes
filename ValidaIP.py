ip_address=input("Ingrese una direeción IP: ")
#remueve caracteres especiales al principio y al final del texto. 
ip_address=ip_address.strip()
#Creamos una bandera de acción
ip_address_flag=True
#verificamos que la ip ingresada solo tenga 3 puntos. 
if (not(ip_address.count('.') == 3)): 
    ip_address_flag=False
else:
    #Validamos que cada uno de los octetos tenga valores entre 0 y 255    
    ip_address=ip_address.split(".") 
    for val in ip_address:
        val=int(val)
        if (not(0 <= val <=255)):
            ip_address_flag=False
    #Preparamos el mensaje 
if (ip_address_flag):
   print ("La IP ingresada es correcta")
else:
    print ("La IP ingresada es incorrecta")