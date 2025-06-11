import socket
import threading

def receber_mensagens(socket_client):
    while True:
        try:
            mensagem = socket_client.recv(1024).decode('utf-8')
            print("\n" + mensagem +"\ndigite mensagem: ", end="")
        except:
            print("\nconexão com o servidor perdida")
            break

def iniciar_cliente():
    host = "10.10.29.112"
    porta = 1026
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host,porta))

        print(s.recv(1024).decode('utf-8'), end="")
        usuario = input()
        s.sendall(usuario.encode('utf-8'))

        print(s.recv(1024).decode('utf-8'), end="")
        senha = input()
        s.sendall(senha.encode('utf-8'))

        resposta = s.recv(1024).decode('utf-8')
        if resposta != "AUTENTICACAO OK":
            print("falha na autenticação")
            return
        
        print("autenticaçao com sucesso! comandos disponiveis:")
        print("HORA - solicitar a hora atual")
        print("DATA - solicitar data atual")
        print("@usuario mensagem - mensagem privada")

        thread_receber = threading.Thread(target=receber_mensagens, args=(s,))
        thread_receber.start()

        while True:
            mensagem = input(" ")
            if mensagem.lower() == "sair":
                break
            s.sendall(mensagem.encode('utf-8'))
            
if __name__ == "__main__":
    iniciar_cliente()
