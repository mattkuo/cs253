import os
from database import Post
from ..BaseHandler import Handler

class NewPostHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(NewPostHandler, self).__init__(os.path.dirname(__file__), "new_post.html", *args, **kwargs)

    def get(self, post_id):
        post_lookup = Post.get_by_id(int(post_id))

        if post_lookup:
            self.render(post_lookup=post_lookup)

        else:
            self.write("Sorry, Post could not be found. Please try again.")
