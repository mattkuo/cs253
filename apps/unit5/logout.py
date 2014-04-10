import os
from .. BaseHandler import Handler

class LogoutHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(LogoutHandler, self).__init__(os.path.dirname(__file__), "welcome.html", *args, **kwargs)

    def get(self):
        user_cookie = self.request.cookies.get('user_id')

        if user_cookie:
            self.response.headers.add_header('Set-Cookie', 'user_id=%s; Path=/' % "")
        self.redirect("/unit4/signup")
