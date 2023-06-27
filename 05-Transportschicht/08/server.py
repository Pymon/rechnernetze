#!/usr/bin/python3
#-*- coding: utf-8 -*-

import socket
from threading import Thread
from datetime import datetime


SERVER_PORT = 8080
SENDING_INTERVAL_SECS = 1


class TimeServer(socket.socket):
    def __init__(self, port=SERVER_PORT):
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM)
        self.bind(("", port))
        self.clients = {}
        self.sending_thread = Thread(target=TimeServer.send_time, args=(self,))
        self.running = False

    def run(self):
        self.running = True
        self.sending_thread.start()
        print(f"[+] Server started on port {SERVER_PORT}\n")
        while True:
            try:
                _, addr = self.recvfrom(0)
                if addr not in self.clients:
                    self.clients[addr] = datetime.now()
                    print(f"[+] Added client {addr} at {self.clients[addr]}")
            except KeyboardInterrupt:
                print("\n[-] Server closed.")
                break
        self.running = False

    def send_time(self):
        t_start = datetime.now()
        while self.running:
            if (datetime.now() - t_start).seconds >= SENDING_INTERVAL_SECS:
                for addr in self.clients:
                    t = datetime.now()
                    seconds_connected = (t - self.clients[addr]).seconds
                    self.sendto(bytes(f"{t.hour}:{t.minute}:{t.second} {seconds_connected}", "utf-8"), addr)
                t_start=datetime.now()


if __name__ == "__main__":
    server = TimeServer()
    server.run()

