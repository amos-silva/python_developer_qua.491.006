import os
import platform
import psutil
import socket


print("INFORMAÇÕES DO COMPUTADOR:\n")
print(f"Sistema Operacional: {platform.system()} {platform.release()}")
print(f"Nome do Usuario Logado: {os.environ.get("USERNAME")}")
print(f"Ip da Máquina: {socket.gethostbyname(socket.gethostname())}\n")

print("Portas Abertas no PC:")
connectall = psutil.net_connections(kind="inet")
only_udp = [conn for conn in psutil.net_connections(kind="inet") if conn.type == socket.SOCK_DGRAM]

# Separa informações sobre as portas
only_tcp_listening_ports = [conn.laddr.port for conn in connectall if conn.status == psutil.CONN_LISTEN]
only_udp_listening_ports = [conn.laddr.port for conn in only_udp]

# remover portas repetidas
only_tcp_listening_ports = list(set(only_tcp_listening_ports))
only_udp_listening_ports = list(set(only_udp_listening_ports))

# organiza as portas na sequencia
only_tcp_listening_ports.sort()
only_udp_listening_ports.sort()

print("TCP:\n")
for port in only_tcp_listening_ports:
    print({port})

print("UDP:\n")
for port in only_udp_listening_ports:
    print({port})