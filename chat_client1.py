#!/usr/bin/python3.5
from socket import *
# serverHost = "127.0.0.1"
#ip cloud
serverHost = "130.211.185.95"
serverPort = 50007

name = input("Informe seu Nome: ")

while True:
    send = input("Digite sua mensagem:")

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
