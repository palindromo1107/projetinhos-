import socket
import threading

def receber_mensagens(conn):
    while True:
        try:
            mensagem = conn.recev(1024).decode()
            if mensagem:
                print(f"\n[recebido] {mensagem}")
        except:
            break

def iniciar_peer(meu_ip, minha_porta, ip_remoto, porta_remota):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.bind((meu_ip, minha_porta))
    servidor.listen(1)
    print(f"[esperando conexao em {meu_ip}:{minha_porta}]...")

    def aceitar_conexao():
        conn, addr = servidor.accept()
        print(f"[conectado por {addr}]")
        threading.Thread(target=receber_mensagens, args=conn, daemon=True).start()
        return conn

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((ip_remoto, porta_remota))
        print(f"[conectado ao peer {ip_remoto}:{porta_remota}]")
    except Exception as e:
        print(f"[erro ao conectar: {e}]")
        cliente = None

    conexao_recebida = aceitar_conexao()

    while True:
        msg = input("voce: ")
        if cliente:
            try:
                cliente.send(msg.encode())
            except:
                print("[erro ao enviar para peer remoto]")
        try:
            conexao_recebida.send(msg.encode())
        except:
            print("[erro ao enviar para conexao recebida]")

if __name__ == "__main__":
    iniciar_peer("localhost", 5000, "localhost", 5001)
