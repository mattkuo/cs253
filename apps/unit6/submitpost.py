import os
from database import Post
from .. BaseHandler import Handler

class SubmitPostHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(SubmitPostHandler, self).__init__(os.path.dirname(__file__), "submit_post.html", *args, **kwargs)
        
    def get(self):
        self.render()

    def post(self):
        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            post_db = Post(subject = subject, content = content)
            post_db.put()

            post_url = str(post_db.key().id())
            self.redirect("/unit6/blog/%s" % post_url)
        else:
            self.render(subject = subject, content = content,
                error = "Please make sure both fields are submitted correctly")