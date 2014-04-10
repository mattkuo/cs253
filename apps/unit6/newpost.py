import os
import time
from google.appengine.api import memcache
from database import Post
from ..BaseHandler import Handler

def last_queried(post_id, update = False):
    key = str(post_id)
    last_queried = memcache.get(key)

    if last_queried is None or update:
        memcache.set(key, time.time())
        return 0
    else:
        return int(time.time() - last_queried)

class NewPostHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(NewPostHandler, self).__init__(os.path.dirname(__file__), "new_post.html", *args, **kwargs)

    def get(self, post_id):
        post_lookup = Post.get_by_id(int(post_id))

        if post_lookup:
            queried = last_queried(post_id)
            self.render(post_lookup=post_lookup, last_queried = queried)

        else:
            self.write("Sorry, Post could not be found. Please try again.")
