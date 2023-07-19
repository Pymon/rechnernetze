#!/usr/bin/python3
#! -*- coding: utf-8 -*-

import socket

IP = "127.0.0.1"
PORT = 85
RECV_BUFFER = 1024

class HttpServer(socket.socket):
    def __init__(self, ip, port):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM)
        self.bind((ip, port))
        self.amount = 1000

    def run(self):
        self.listen(1)
        while True:
            conn, addr = self.accept()
            data = self.recvline(conn)
            response = self.handle_request(data)
            conn.send(response)
            conn.close()

    def recvline(self, conn) :
        data = str(conn.recv(RECV_BUFFER)).split("\r\n")[0]
        return data

    def handle_request(self, request):
        path = request.split(" ")[1]
        print(path)
        if path == "/":
            return b"HTTP/1.0 200 OK\r\n\r\n" + bytes(open("page.html", "r").read(), "utf-8")
        elif path == "/one":
            self.amount -= 1
            print("one")
        elif path == "/five":
            self.amount -= 5
        elif path == "/ten":
            self.amount -= 10
        else:
            return b"HTTP/1.0 404 Not Found\r\n\r\n<h1>Spast</h1>\n"
        html = f"HTTP/1.0 200 OK\r\n\r\n<h1>Remaining</h1><hr><p>Still {self.amount} pieces</p>"
        return bytes(html, "utf-8")

server = HttpServer(IP, PORT)
server.run()