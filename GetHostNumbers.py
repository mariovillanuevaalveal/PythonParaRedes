# 
# Este código obtiene las direcciones de host disponible a partir de una direccion de red.
# esta última ingresada por teclado
#
import ipaddress

host = ipaddress.ip_network(input("Ingrese una dirección de red en el sigiente formato X.X.X.X/X "))
print (f"Esta red tiene disponible  {host.num_addresses-2} ")
