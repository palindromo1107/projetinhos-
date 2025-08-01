import socket
import threading
import time
nome = input("Digite seu nome de usuário: ")
porta_escuta = int(input("Digite sua porta de escuta (ex: 5000): "))
todos_peers = [
    ('localhost', 5000),
    ('localhost', 5001),
    ('localhost', 5002),
    ('localhost', 5003)
]
conexoes = []

def escutar():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind(('localhost', porta_escuta))
    servidor.listen(10)
    print(f"[{nome}] Escutando em localhost:{porta_escuta}...")
    while True:
        conn, addr = servidor.accept()
        conexoes.append(conn)
        threading.Thread(target=receber_mensagens, args=(conn,), daemon=True).start()

def receber_mensagens(conn):
    while True:
        try:
            dados = conn.recv(1024)
            if not dados:
                break
            print("\n" + dados.decode())
        except:
            break

def conectar_peers():
    for ip, porta in todos_peers:
        if porta == porta_escuta:
            continue
        conectado = False
        while not conectado:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((ip, porta))
                conexoes.append(s)
                print(f"[{nome}] Conectado a {ip}:{porta}")
                conectado = True
            except:
                time.sleep(2)

def enviar_mensagem(msg):
    for conn in conexoes:
        try:
            conn.send(f"{nome}: {msg}".encode())
        except:
            pass

threading.Thread(target=escutar, daemon=True).start()
threading.Thread(target=conectar_peers, daemon=True).start()

while True:
    texto = input()
    if texto.strip().lower() == "sair":
        break
    enviar_mensagem(texto)
