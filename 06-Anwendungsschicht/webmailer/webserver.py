from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from http.cookies import SimpleCookie
from http import HTTPStatus
import logging


logging.basicConfig(format='[%(levelname)s][%(module)s] %(message)s', level=logging.DEBUG)


SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route, args = self._parse_path()
        if route in self.server.routes:
            self.server.routes[route](self, args)
        else:
            if "#404" in self.server.routes:
                self.server.routes["#404"](self)
            else:
                self._handle_404()

    def redirect(self, location, cookies={}):
        return self._build_header(HTTPStatus.TEMPORARY_REDIRECT, cookies=cookies, header_fields={"Location": location}, )

    def render(self, template, context={}, cookies={}):
        self._build_header(cookies=cookies)
        self.wfile.write(self._render_template(
            template, context).encode('ascii', 'xmlcharrefreplace'))

    def get_cookies(self):
        return SimpleCookie(self.headers.get('Cookie'))

    def _set_cookie(self, key, value):
        cookie = SimpleCookie()
        cookie[key] = value
        self.send_header("Set-Cookie", cookie[key].OutputString())

    def _handle_404(self):
        self._build_header(HTTPStatus.NOT_FOUND)

    def _build_header(self, status_code: int = HTTPStatus.OK, cookies: dict = {}, header_fields: dict = {}):
        self.send_response(status_code)
        for cookie in cookies:
            self._set_cookie(cookie, cookies[cookie])
        for key, value in header_fields.items():
            self.send_header(key, value)
        self.end_headers()

    def _render_template(self, template_file_name: str, context: dict):
        with open(template_file_name) as template_file:
            template_raw = template_file.read()
            return template_raw.format(**context)

    def _parse_path(self):
        path = self.path.split("?")
        args = None
        if len(path) > 1 and path[1] != "":
            args = {}
            for argstr in path[1].split("&"):
                kv_pair = argstr.split("=")
                if len(kv_pair) > 1:
                    args[kv_pair[0]] = kv_pair[1]
                else:
                    args[kv_pair[0]] = None
        return path[0], args

class CustomHTTPServer(ThreadingHTTPServer):
    def __init__(self, routes, server_address=(SERVER_IP, SERVER_PORT), handler_class=CustomHTTPRequestHandler):
        super().__init__(server_address, handler_class)
        self.routes = routes
        self.url = f"http://{server_address[0]}:{server_address[1]}"
    
    def serve_forever(self):
        logging.info(f"Server started on {self.url}")
        super().serve_forever()