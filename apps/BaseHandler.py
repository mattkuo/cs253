import webapp2
import os
import jinja2


class Handler(webapp2.RequestHandler):
    def __init__(self, template_path, template, *args, **kwargs):
        super(Handler, self).__init__(*args, **kwargs)
        self.jinja_environment = jinja2.Environment(autoescape=True,
            loader=jinja2.FileSystemLoader(os.path.join(template_path, "templates")))
        self.retrieved_template = self.jinja_environment.get_template(template)

    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render(self, **kw):
        self.response.out.write(self.retrieved_template.render(**kw))