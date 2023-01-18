# Este codigo imprime todas las direcciones ip 
# pertenecientes a una dirección de red dada por teclado. 
# Utilizacion de libreria ipaddress de python
import ipaddress
RedIp = ipaddress.ip_network(input("Ingrese una dirección de red en el sigiente formato X.X.X.X/X "))
print (f"Los host que pertenesen a la red {RedIp} son > ")
for x in RedIp.hosts():
    print (x)


