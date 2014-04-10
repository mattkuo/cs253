import os
from .. BaseHandler import Handler
from google.appengine.api import memcache

class FlushHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(FlushHandler, self).__init__(os.path.dirname(__file__), "template.html", *args, **kwargs)

    def get(self):
        memcache.flush_all()
        self.redirect('/unit6/blog')
