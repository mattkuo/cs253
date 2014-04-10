import re
import os
from .. BaseHandler import Handler
from hasher import SaltHasher
from database import Users
from google.appengine.ext import db

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
MAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")


class SignupHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(SignupHandler, self).__init__(os.path.dirname(__file__), "signup.html", *args, **kwargs)

    def get(self):
        self.render()

    def post(self):
        error = ""

        get_username = self.request.get("username")
        get_password = self.request.get("password")
        get_verify = self.request.get("verify")
        get_email = self.request.get("email")

        if get_email and not MAIL_RE.match(get_email):
            error = "Invalid e-mail"

        if get_password != get_verify:
            error = "Passwords do not match."

        if not PASS_RE.match(get_password):
            error = "Invalid password."

        if not USER_RE.match(get_username):
            error = "Invalid Username. Please try again."

        if db.GqlQuery("SELECT __key__ FROM Users WHERE username = :1", get_username).count() != 0:
            error = "User already exists. Please choose a different username"

        if error:
            self.render(username=get_username, password=get_password, verify=get_verify, email=get_email, error=error)
        else:
            hashed_result = SaltHasher(get_password)
            user_db = Users(username=get_username, password=hashed_result.get_result()[0], email=get_email, salt=hashed_result.get_result()[1])
            user_db.put()

            user_id = str(user_db.key().id())
            self.response.headers.add_header('Set-Cookie', 'user_id=%s|%s; Path=/' % (user_id, hashed_result.get_result()[0]))
            self.redirect("/unit5/blog/welcome")