import socket

def pack(_id, qr, opcode, flags, z, rcode, qdcount, ancount, nscount, arcount, requested_domain_name: str, qtype, qclass):
    data = []
    data.append((_id).to_bytes(2))
    data.append((qr << 15 + opcode << 11 + flags << 7 + z << 4 + rcode).to_bytes(2))
    data.append((qdcount).to_bytes(2))
    data.append((ancount).to_bytes(2))
    data.append((nscount).to_bytes(2))
    data.append((arcount).to_bytes(2))

    for label in requested_domain_name.split("."):
        data.append((len(label)).to_bytes(1))
        data.append(label.encode("ascii"))
    data.append((0).to_bytes(1))  # terminate labels from domain name
    data.append((qtype).to_bytes(2))
    data.append((qclass).to_bytes(2))
    
    return(b"".join(data))

data = pack(
    1,
    0b0,
    0b000,
    0b000,
    0b000,
    0b000,
    1,
    0,
    0,
    0,
    "www.tu-chemnitz.de",
    1,
    1
    )

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
DNS_IP = "134.109.133.1"
PORT = 53

message = data
addr = (DNS_IP, PORT)

sock.sendto(message, addr)

data, server = sock.recvfrom(1024)

print(f"Data:\n{data}")
print(f"Server:\n{server}")
print()

rr = data[len(message):]
_type = int(rr[2]+rr[3])
_class = int(rr[4]+rr[5])
print(f"type: {_type}")
print(f"class: {_class}")

ip = rr[12:16]
ip = ".".join([str(octett) for octett in ip])
print(f"IP Address: {ip}")

# print(type_, class_, len_)
# print(len)
# print(rr[11:11+len].decode)
