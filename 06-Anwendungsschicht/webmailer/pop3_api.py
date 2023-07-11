import email
import logging
from poplib import POP3, error_proto

logging.basicConfig(
    format="[%(levelname)s][%(module)s] %(message)s", level=logging.DEBUG
)


class ConnectionException(Exception):
    pass


class AuthenticationException(Exception):
    pass


class SessionNotAuthenticated(Exception):
    pass


class POP3Connection(POP3):
    def __init__(self, host, port):
        """Provides simple API for specific functions"""
        super().__init__(host, port)

    def authenticate(self, username, password):
        """Authenticates against POP3 server"""
        try:
            self.user(username)
            self.pass_(password)
            logging.info(f"User {username} authenticated successfully")
        except error_proto:
            logging.warning(f"User {username} failed to authenticate")
            raise AuthenticationException("Invalid password")

    def get_stat(self):
        """Get stat info from server"""
        try:
            return super().stat()
        except error_proto:
            raise SessionNotAuthenticated

    def get_table_info(self, mail_id):
        """Get specific data for mailbox rendering"""
        header = super().top(mail_id, 0)
        header = email.message_from_bytes(b"\n".join(header[1]))
        return header.get("From"), header.get("Subject"), header.get("Date")

    def get_mail(self, mail_id):
        """Get mail as email object"""
        mail = super().retr(mail_id)
        return email.message_from_string(
            "\n".join(mail.decode("utf-8") for mail in mail[1])
        )


class POP3ConnectionHandler:
    """Handles multiple connections to a POP3 server"""

    def __init__(self):
        self.connections = {}

    def connect(self, username, password=None, server=None, port=None):
        """Adds connection if not already existing"""
        if username in self.connections:
            if not self.is_connected(username):
                raise SessionNotAuthenticated
        else:
            self._add_connection(username, password, server, port)
        return self.connections[username]

    def disconnect(self, username):
        """Disconnects from server, deletes connection"""
        if self.is_connected:
            self.connections[username].quit()
        if username in self.connections:
            del self.connections[username]

    def is_connected(self, username):
        """Checks if connection to server is active"""
        if username in self.connections:
            try:
                self.connections[username].get_stat()
                return True
            except SessionNotAuthenticated:
                pass
        return False

    def _add_connection(self, username, password, server, port):
        """Authenticates against POP3 server"""
        try:
            connection = POP3Connection(server, port)
        except:
            raise ConnectionException
        connection.authenticate(username, password)
        self.connections[username] = connection
        return self.connections[username]
