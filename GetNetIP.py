# 
# Este código obtiene la dirección de red a partir de una direccion de host 
# esta última ingresada por teclado
#
import ipaddress

host = ipaddress.ip_interface(input("Ingrese una dirección de host en el sigiente formato X.X.X.X/X "))
print (f"La dirección de red del Host {host} es {host.network}  ")
