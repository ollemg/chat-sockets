#!/usr/bin/python3.5
from socket import *
#Pega o ip da interface
getip = socket(AF_INET, SOCK_DGRAM)
getip.connect(("8.8.8.8", 80))
ip = getip.getsockname()[0]
getip.close()
print(ip)

serverHost = ip
serverPort = 50007

resposta = ""

nome = input("Informe seu Nome: ")

while True:
    if resposta != "":
        print("Resposta: ", resposta)

    envio = input("Digite sua mensagem:")

    socketClient = socket(AF_INET, SOCK_STREAM)
    socketClient.connect((serverHost, serverPort))

    envio = ("%s disse: " %nome + envio)
    binario = str.encode(envio)
    #for line in envio:
    socketClient.send(binario)

    idSession = socketClient.recv(30)
    resposta = socketClient.recv(1024)

    print("Resposta: ", resposta)
    print("ID: ", idSession)

socketClient.close()
