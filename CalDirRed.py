def get_network_address(ip, subnet_mask):   
    ip_octets = ip.split(".")
    mask_octets = subnet_mask.split(".")
    network_address = []
    for i in range(4):
       # print(ip_octets[i], "\n")
        print((int(ip_octets[i]) & int(mask_octets[i])), "\n")
        network_address.append(str(int(ip_octets[i]) & int(mask_octets[i])))
    return ".".join(network_address)

ip = "192.168.1.5"
subnet_mask = "255.0.0.0"
network_address = get_network_address(ip, subnet_mask)
print(network_address)
