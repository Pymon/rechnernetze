#!/usr/bin/python3
#-*- coding: utf-8 -*-

from poplib import POP3, error_proto
import logging
import email

logging.basicConfig(format='[%(levelname)s][%(module)s] %(message)s', level=logging.DEBUG)

SERVER_ADDRESS = "taurus.informatik.tu-chemnitz.de"
SERVER_PORT = 110

class AuthenticationException(Exception): pass
class SessionExpiredException(Exception): pass

class POP3Connection(POP3):
    def __init__(self, host=SERVER_ADDRESS, port=SERVER_PORT):
        super().__init__(host, port)
    
    def authenticate(self, username, password):
        try:
            self.user(username)
            self.pass_(password)
            logging.info(f"User {username} authenticated successfully")
        except error_proto:
            logging.warning(f"User {username} failed to authenticate")
            raise AuthenticationException("Invalid password")
    
    def get_stat(self):
        try:
            return super().stat()
        except error_proto:
            raise Exception
        
    def get_table_info(self, mail_id):
        try:
            header = super().top(mail_id, 0)
            header = email.message_from_bytes(b"\n".join(header[1]))
            return header.get("From"), header.get("Subject"), header.get("Date")
        except error_proto:
            raise Exception
    
    def get_mail(self, mail_id):
        try:
            mail = super().retr(mail_id)
            return email.message_from_bytes(b"\n".join(mail[1]))
        except error_proto:
            raise Exception
        


class POP3ConnectionHandler():
    def __init__(self):
        self.connections = {}
    
    def connect(self, username, password=None):
        if username in self.connections:
            if not self._is_active(username):
                raise SessionExpiredException
        else:
            self._add_connection(username, password)
        return self.connections[username]

    def _add_connection(self, username, password):
        connection = POP3Connection()
        connection.authenticate(username, password)
        self.connections[username] = connection
        return self.connections[username]

    def _is_active(self, username):
        return True

    def _renew_connection(self, username, password):
        pass

    def _quit_connection(self, username):
        pass

if __name__ == "__main__":
    pop3_handler = POP3ConnectionHandler()
    try:
        pop3 = pop3_handler.connect("rot", "rot")
        pop3.get_table_info(1)
    except AuthenticationException as e:
        logging.warning(e)