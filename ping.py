import os

ip = "172.16.1.1"

echo_request = os.popen(f"ping -t 4 {ip} ").read()
if ("icmp_seq=3") in echo_request: 
    print ("Full Ping")
print (echo_request)
print ("Fin")