#################################################################################
# Ejercicio Condicional IF /else
# Este código pide por teclado una dirección IP                                 #
# Conprueba mediante IF si cada octeto es correcto                              #
# Si todos son correctos envía una sálida en pantalla que la IP es correcta.    #
#                                                                               #
#################################################################################
octetos=[]
ip_add = input (" Ingrese una dirección IP : ")
# Utilización del metodo split()
octetos = ip_add.split(".")
if int(octetos[0]) > 0 and int(octetos[0]) < 255 :
    print (octetos[0] + " es correcto en el primer octeto")
else : 
    print ("El octeto es Incorrecto ")
if int(octetos[1]) > 0 and int(octetos[1]) < 255 :
    print (octetos[1] + " es correcto en el Segundo octeto")
else : 
    print ("El octeto es Incorrecto ")
if int(octetos[2]) > 0 and int(octetos[2]) < 255 :
    print (octetos[2] + " es correcto en el Tercer octeto")
else : 
    print ("El octeto es Incorrecto ")
if int(octetos[3]) > 0 and int(octetos[3]) < 255 :
    print (octetos[3] + " es correcto el Cuarto octeto")
else : 
    print ("El octeto es Incorrecto ")
