#!/usr/bin/python3
# -*- coding: utf-8 -*-

import html
import sys

import infobox
import pop3_api
from webserver import CustomHTTPRequestHandler, CustomHTTPServer


def protected_route(func):
    def inner(*args):
        if args[0].user_is_logged_in():
            return func(*args)
        return args[0].redirect("/login")

    return inner


class Webmailer(CustomHTTPRequestHandler):
    def index(self, args):
        self.redirect("/login")

    def login(self, args):
        if self.user_is_logged_in():
            self.redirect("/mailbox")
            return
        context = {"program_name": "Webmailer"}
        if not args:
            self.render("login.html", context)
        else:
            username = args.get("username")
            password = args.get("password")
            if not username or not password:
                context["infobox-area"] = infobox.Infobox(
                    infobox.WARNING,
                    "<b>Bitte geben Sie Benutzername und Passwort ein</b>",
                ).render()
                self.render("login.html", context)
                return
            try:
                pop3.connect(username, password)
                self.redirect("/mailbox", cookies={"username": username})
            except pop3_api.AuthenticationException:
                context["infobox-area"] = infobox.Infobox(
                    infobox.ERROR,
                    "<b>Anmeldung fehlgeschlagen:</b> Bitte erneut versuchen.",
                ).render()
                self.render("login.html", context)

    @protected_route
    def mailbox(self, args):
        print(args)
        if not args:
            username = self.get_cookies().get("username").value
            mailbox = pop3.connect(username)
            mails_total, size_total = mailbox.get_stat()
            table_entries = "<tr><th>Absender</th><th>Betreff</th><th>Datum</th></tr>"
            for mail_id in range(1, mails_total + 1):
                from_, subject, date = mailbox.get_table_info(mail_id)
                table_entries += f"<tr><td>{from_}</td><td><a href='/mailbox?id={mail_id}'><b>{subject}</b></a></td><td>{date}</td></tr>"
            greeting = (
                mailbox.getwelcome()
                .decode("ascii")
                .replace("+OK ", "")
                .replace(" starting.", "")
            )
            context = {
                "username": username,
                "mails_total": mails_total,
                "size_total": size_total,
                "table_entries": table_entries,
                "greeting": greeting,
            }
            self.render("mailbox.html", context)
        else:
            self.detail(args)

    @protected_route
    def detail(self, args):
        username = self.get_cookies().get("username").value
        mail_id = args.get("id")
        mailbox = pop3.connect(username)
        mail = mailbox.get_mail(mail_id)
        context = {
            "mail_id": mail_id,
            "subject": mail.get("Subject"),
            "from": mail.get("From"),
            "payload": html.escape(mail.get_payload()).replace("\n", "<br>"),
        }
        self.render("detail.html", context)

    @protected_route
    def logout(self, args):
        username = self.get_cookies().get("username").value
        pop3.disconnect(username)
        cookies = {"username": "deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT"}
        self.redirect("/login", cookies=cookies)

    def user_is_logged_in(self):
        user_cookie = self.get_cookies().get("username")
        if user_cookie:
            return pop3.is_connected(user_cookie.value)
        return False


ROUTES = {
    "/": Webmailer.index,
    "/login": Webmailer.login,
    "/mailbox": Webmailer.mailbox,
    "/logout": Webmailer.logout,
}


if __name__ == "__main__":
    global pop3
    pop3 = pop3_api.POP3ConnectionHandler()
    server = CustomHTTPServer(ROUTES, handler_class=Webmailer)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        sys.exit(1)
    except Exception as e:
        raise e
