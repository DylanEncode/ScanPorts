import sys
import socket
import colorama
import pyfiglet
from colorama import *
#colores
rojo = Fore.RED
verde = Fore.GREEN
reset = Fore.WHITE
ascii = pyfiglet.figlet_format(f"Scan ports ~")
print(ascii)
print("By dylan ~")
ip = socket.gethostbyname(input("Ingrese la IP : "))

print("Escaneando objetivo " + ip + " Esto puede tomar un tiempo")

try:
    for port in range(1,150):
        escaneo = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
        resultado = escaneo.connect_ex((ip, port))
        if resultado == 0:
            print(f"El puerto {verde}{reset} esta abierto".format(port))
            escaneo.close()
except:
    print("\n Terminando escaneo...")
    sys.exit(0)
