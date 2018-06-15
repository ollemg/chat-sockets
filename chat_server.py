from socket import *

hostServidor = '10.8.43.245'
#hostServidor = '127.0.0.1'
portaServidor = 51234

#Objeto Servidor Criado
socketServidor = socket(AF_INET, SOCK_STREAM)

#Vinculando Servidor a uma porta ...
socketServidor.bind((hostServidor, portaServidor))

while True:
    #Na escuta...resposta = socketClient.recv(1024)
    socketServidor.listen(10)

    #servidor aceita solicitacao?
    #sim, retorna: a conexao e o "id" do cliente
    connection, id = socketServidor.accept()
    #print('Server acessado por', id)
    idSession = str.encode(str(id))

    #recebendo dado do cliente
    data = connection.recv(1024)

    print(data)

    #enviando a mensagem recebido novamente
    connection.send(idSession)
    connection.send(data)

#connection.close()
