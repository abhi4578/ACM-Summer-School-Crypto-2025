import struct
import json

def recvall(sock, n):
    buf = b''
    while len(buf) < n:
        chunk = sock.recv(n - len(buf))
        if not chunk:
            raise ConnectionError("socket closed early")
        buf += chunk
    return buf

def send_string(sock, text):
    data   = text.encode('utf-8')
    header = struct.pack('>I', len(data))
    sock.sendall(header + data)
    
def recv_string(sock):
    header = recvall(sock, 4)
    length = struct.unpack('>I', header)[0]
    data   = recvall(sock, length)
    return data.decode('utf-8')
    
def send_json(sock, data):
    send_string(sock, json.dumps(data))
    
def recv_json(sock):
    return json.loads(recv_string(sock))

def send_bytes(sock, data):
    header = struct.pack('>I', len(data))
    sock.sendall(header + data)

def recv_bytes(sock):
    header = recvall(sock, 4)
    length = struct.unpack('>I', header)[0]
    return recvall(sock, length)