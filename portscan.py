#PortScan Script
#Curso Introdução a Pentest

import socket

portas = [21, 22, 23, 443, 80, 8080, 53, 587, 110, 8443] #Lista de portas a serem scaneadas

for i in portas:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Criar um socket para conexão
    client.settimeout(0.5) # timeout
    cod = client.connect_ex(('bancocn.com',i)) #seta o alvo e a porta atual a ser testado
    if cod == 0:
        status_porta = "Open"
    else:
        status_porta = "Close"
    print "Porta:",i,status_porta


