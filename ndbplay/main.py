import webapp2
from BaseHandler import BaseHandler
from BaseHandler import config
import os

import jinja2
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


# [START main_page]
class MainPage(BaseHandler):
    def get(self):

        # these are the values that will be fed into the Jinja2 HTML template
        template_values = {
            'title': "Playing with Jinja and NDB"
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))

# [END main_page]


# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/', MainPage),
], config=config, debug=True)