import os
import re
import json
from database import Post
from ..BaseHandler import Handler

PERMALINK_RE = re.compile(r"^[0-9]+$")

class JsonFeedHandler(Handler):
    def __init__(self, *args, **kwargs):
        super(JsonFeedHandler, self).__init__(os.path.dirname(__file__), "welcome.html", *args, **kwargs)

    def get(self, request):
        self.response.headers["Content-Type"] = "application/json; charset-UTF-8"
        response = ""
        # determine if blog or permalink
        if not request:
            query = Post.gql("ORDER BY created DESC LIMIT 10")
            results = []

            for post in query:
                result = {
                "content": post.content,
                "created": post.created.strftime("%a %b %e %T %Y"),
                "last_modified": post.created.strftime("%a %b %e %T %Y"),
                "subject": post.subject
                }
                results.append(result)
            response = json.dumps(results)

        elif PERMALINK_RE.match(request):
            post = Post.get_by_id(int(request))
            result = {
            "content": post.content,
            "created": post.created.strftime("%a %b %e %T %Y"),
            "last_modified": post.created.strftime("%a %b %e %T %Y"),
            "subject": post.subject
            }
            response = json.dumps(result)

        if response:
            self.write(response)
        else:
            self.write("Error processing request")
        
