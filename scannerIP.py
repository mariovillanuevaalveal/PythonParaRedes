import socket
b_Loop = True
respuesta = "y"
def scan_ports(ip, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


while ( b_Loop == True) and (respuesta == "y"):
    ip = input("Ingrese la IP que sera escaneada. ")
    start_port = int(input ("ingrese el puerto de inicial "))
    
    if (start_port < 1 ):
        print("Número ingresado incorrecto. ")
        break
    end_port = int( input("Ingrese puerto final  "))
    if end_port < start_port or end_port > 65535:
            print("Número de puerto ingresado incorrecto ") 
            break
    else:
        open_ports = scan_ports(ip, start_port, end_port)
        print(open_ports)
    respuesta = input ("Desea realizar otro escaneo 'y'")

print ("Adios \n")
    