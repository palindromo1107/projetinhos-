import socket

def start_server():
    host = "10.10.29.112"
    port = 1025
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host,port))
        server_socket.listen(1)
        print(f"servidor iniciado. aguardando conexao em {host}:{port}")
        conn,addr = server_socket.accept()
        with conn:
            print(f"conexao estabelecida com {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                mensagem = data.decode('utf-8')
                print(f"mensagem recebida do cliente: {mensagem}")
                resposta = input("responda; ") ## ilustrativo
                conn.sendall(resposta.encode('utf-8'))
        print("conexao encerrada")
if __name__ == "__main__":
    start_server()
