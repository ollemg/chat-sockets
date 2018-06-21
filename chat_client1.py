#!/usr/bin/python3.6
from socket import *
#Pega o ip da interface
getip = socket(AF_INET, SOCK_DGRAM)
getip.connect(("8.8.8.8", 80))
ip = getip.getsockname()[0]

serverHost = ip
serverPort = 50007

name = input("Informe seu Nome: ")
print("Digite 'sair' para fechar!")

while True:
    send = input("Digite sua mensagem: ")

    if send == 'sair' or send == 'SAIR':
        break

    socketClient = socket(AF_INET, SOCK_STREAM)
    socketClient.connect((serverHost, serverPort))

    send = ("%s disse: " %name + send)
    bin = str.encode(send)
    #for line in send:
    socketClient.send(bin)

    idSession = socketClient.recv(30)

    reply = socketClient.recv(1024)

    with open('historico.txt', 'a+') as hist:
        hist.write("\n")
        hist.write(str(send))
    hist.close()

    with open('historico.txt', 'r') as talk:
        chat = talk.readlines()
    talk.close()

    print("Resposta: ", chat)

    socketClient.close()
getip.clone()
