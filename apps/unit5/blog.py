import os
from .. BaseHandler import Handler
from google.appengine.ext import db

class BlogHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(BlogHandler, self).__init__(os.path.dirname(__file__), "blog.html", *args, **kwargs)
        
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 10")
        self.render(posts=posts)


