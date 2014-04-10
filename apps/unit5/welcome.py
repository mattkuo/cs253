import os
from database import Users
from google.appengine.ext import db
from .. BaseHandler import Handler

class WelcomeHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(WelcomeHandler, self).__init__(os.path.dirname(__file__), "welcome.html", *args, **kwargs)
        
    def get(self):
        user_cookie = self.request.cookies.get("user_id")

        if user_cookie:
            user_id, hashed_result = user_cookie.split("|")

            query = Users.get_by_id(int(user_id))

            if query:
                username = query.username
                user_hashed_pw = query.password

                if user_hashed_pw == hashed_result:
                    self.render(username="Welcome, " + username)
                    return
        self.redirect("/unit5/blog/signup")