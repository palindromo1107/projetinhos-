import socket
import threading
import time
from datetime import datetime
HOST='123.0.0.1'
PORTA= 12349
USUARIOS={"aluno": "ifpb1234","admin": "admin123"}
LOGS_FILE="serve_logs.txt"
clientes_conectados =[]
def regisrar_log(mensagem):
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
                            conn.sendall("digite usúario: ". encode('utf-8'))
                            usuario= conn.recv(1234).decode('utf-8').strip()
                            conn.sendall("Digite senha:".encode('utf_8'))
                            senha= conn.recv(1034).decode('utf-8').strip
                            if USUARIOS.get(usuario) != senha:
                                conn.sendall("AUTENTICACAO FALHOU".encode('utf'))
