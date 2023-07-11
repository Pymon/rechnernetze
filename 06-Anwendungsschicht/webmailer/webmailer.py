#!/usr/bin/python3
# -*- coding: utf-8 -*-

from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from http.cookies import SimpleCookie
from http import HTTPMethod, HTTPStatus
import sys
import hashlib
import html

import pop3_api


SERVER_IP = "127.0.0.1"
SERVER_PORT = 8080


class CustomHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        route, args = self._parse_path()
        if route in ROUTES:
            ROUTES[route](self, args)
        else:
            if "#404" in ROUTES:
                ROUTES["#404"](self)
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
        if len(path) > 1:
            args = {}
            for argstr in path[1].split("&"):
                kv_pair = argstr.split("=")
                if len(kv_pair) > 1:
                    args[kv_pair[0]] = kv_pair[1]
                else:
                    args[kv_pair[0]] = None
        return path[0], args


class WebmailerViews(CustomHTTPRequestHandler):
    def index(self, args):
        self.redirect("/login")

    def login(self, args):
        if not args:
            context = {"program_name": "Webmailer"}
            self.render("login.html", context)
        else:
            try:
                username = args.get("username")
                password = args.get("password")
                pop3.connect(username, password)
                self.redirect("/mailbox", cookies={"username": username})
            except pop3_api.AuthenticationException:
                print("FAIL")

    def mailbox(self, args):
        if not args:
            username = self.get_cookies()['username'].value
            mailbox = pop3.connect(username)
            mails_total, size_total = mailbox.get_stat()
            table_entries = "<tr><th>Absender</th><th>Betreff</th><th>Datum</th></tr>"
            for mail_id in range(1, mails_total + 1):
                from_, subject, date = mailbox.get_table_info(mail_id)
                table_entries += f"<tr><td>{from_}</td><td><a href='/mailbox?id={mail_id}'><b>{subject}</b></a></td><td>{date}</td></tr>"
            context = {"username": username,
                       "mails_total": mails_total, "size_total": size_total, "table_entries": table_entries}
            self.render("mailbox.html", context)
        else:
            self.detail(args)
    
    def detail(self, args):
        username = self.get_cookies()['username'].value
        mail_id = args.get("id")
        mailbox = pop3.connect(username)
        mail = mailbox.get_mail(mail_id)
        context = {"mail_id": mail_id, "subject": mail.get("Subject"), "from": mail.get("From"), "payload": html.escape(mail.get_payload())}
        self.render("detail.html", context)


ROUTES = {
    "/": WebmailerViews.index,
    "/login": WebmailerViews.login,
    "/mailbox": WebmailerViews.mailbox,
}


if __name__ == "__main__":
    global pop3
    pop3 = pop3_api.POP3ConnectionHandler()
    server = ThreadingHTTPServer((SERVER_IP, SERVER_PORT), WebmailerViews)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        raise e
