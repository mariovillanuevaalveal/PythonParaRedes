##################################
# convierte una dirección ip a su 
# correspondiente binario
##################################

def ip_to_binary(ip):
    octets = ip.split(".")
    binary_octets = []
    for octet in octets:
        binary_octet = bin(int(octet))[2:].zfill(8)
        binary_octets.append(binary_octet)
    return ".".join(binary_octets)

ip = "192.168.1.1"
binary_ip = ip_to_binary(ip)
print(binary_ip)