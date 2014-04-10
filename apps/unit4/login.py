import os
from hasher import SaltHasher
from .. BaseHandler import Handler
from database import Users
from google.appengine.ext import db


class LoginHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(LoginHandler, self).__init__(os.path.dirname(__file__), "login.html", *args, **kwargs)

    def get(self):
        self.render()

    def post(self):
        get_username = self.request.get("username")
        get_password = self.request.get("password")

        user = db.GqlQuery("SELECT * FROM Users WHERE username=:1", get_username).get()

        if user:
            # Verify password is correct
            user_id = str(user.key().id())
            user_hashedpw = str(user.password)
            user_salt = str(user.salt)

            validation = SaltHasher(get_password, salt=user_salt, hashed_pw=user_hashedpw).get_result()

            if validation:
                # User entered correct password. Set cookie
                self.response.headers.add_header('Set-Cookie', 'user_id=%s|%s; Path=/' % (user_id, user_hashedpw))
                self.redirect("/unit4/welcome")
                return

        self.render(username=get_username, password=get_password, error="Invalid Login. Please try again.")