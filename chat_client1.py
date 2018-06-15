from socket import *
import socket

sessao = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sessao.connect(("8.8.8.8", 80))
print(sessao.getsockname()[0])
ip = sessao.getsockname()[0]
sessao.close()

serverHost = "10.8.43.245"
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
