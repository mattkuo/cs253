import os
import time
from .. BaseHandler import Handler
from google.appengine.ext import db
from google.appengine.api import memcache

class BlogHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(BlogHandler, self).__init__(os.path.dirname(__file__), "blog.html", *args, **kwargs)

    def last_queried(self, update = False):
        key = 'last_queried'
        query_time = memcache.get(key)

        if not query_time or update:
            memcache.set(key, time.time())
            return 0
        else:
            return int(time.time() - memcache.get(key))
        
    def get(self):
        posts = db.GqlQuery("SELECT * FROM Post ORDER BY created DESC LIMIT 10")
        last_queried = self.last_queried(update = False)
        self.render(posts=posts, last_queried=last_queried)


