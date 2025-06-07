import socket
import threading
import time
from datetime import datetime

HOST='123.0.0.1'
PORTA= 12349
USUARIOS={"aluno": "ifpb1234","admin": "admin123"}
LOGS_FILE="serve_logs.txt"
clientes_conectados =[]

def registrar_log(mensagem):
    with open(LOGS_FILE,"a") as log_file:
        log_file.write(f"[{datetime.now()}]{mensagem}\n")

def broadcast (mensagem, origem=None):
    for cliente in clientes_conectados:
        if cliente != origem:
            try:
cliente.sendall(mensagem.encode('utf-8'))
            except:
clientes_conectados.remove(clientes_conectados)
        
def handle_cliente(conn, addr):
    try:
        conn.sendall("digite usuario: ". encode('utf-8'))        
        usuario= conn.recv(1234).decode('utf-8').strip()
        conn.sendall("Digite senha:".encode('utf_8'))

        senha= conn.recv(1034).decode('utf-8').strip
        if USUARIOS.get(usuario) != senha:
            conn.sendall("AUTENTICACAO FALHOU".encode('utf-8'))
            registrar_log(f"Falha na autenticacao de {addr}")
            conn.close()
            return
        conn.sendall("AUTENTICACAO OK".encode('utf-8'))
        clientes_conectados.append(conn)
        registrar_log(f"Novo cliente conectado: {usuario}@{addr}")

        while True:
            dados = conn.recv(1024)
            if not dados:
                break
                                
            mensagem = dados.decode('utf-8').strip()
            registrar_log(f"Mensagem de {usuario}: {mensagem}")

            if mensagem == "HORA":
                resposta = f"HORA {datetime.now().strftime('%H:%M:%S')}"
            elif mensagem == "DATA":
                resposta = f"DATA {datetime.now().strftime('%d/%m/%Y')}"
            elif mensagem.startswith("@"):
                partes = mensagem.split(maxsplit=1)
                destino = partes[0][1:]
                msg = partes[1] if len(partes) > 1 else ""
                resposta = f"PRIVADO {usuario}: {msg}"
            else:
                resposta = f"{usuario}: {mensagem}"
                broadcast(resposta, conn)
                                
                conn.sendall(resposta.encode('utf-8'))
    finally:
        if conn in clientes_conectados:
            clientes_conectados.remove(conn)
        conn.close()
        registrar_log(f"Conexao encerrada: {usuario}@{addr}")

def iniciar_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORTA))
        s.listen()
        registrar_log(f"Servidor iniciado em {HOST}:{PORTA}")
        print("servidor aguardando conexoes...")

        while True:
            conn, addr = s.accept()
            thread = threading.Thread(thread = handle_cliente, args = (conn, addr))
            thread.start()

if __name__ == "__main__":
    iniciar_server()
