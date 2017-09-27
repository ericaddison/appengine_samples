import webapp2
from ndbClasses import MyUser
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
class ListUsers(BaseHandler):
    def get(self):

        user_query = MyUser.query()
        users = list(user_query.fetch())

        print("\n\n" + str(users) + "\n\n")


        # these are the values that will be fed into the Jinja2 HTML template
        template_values = {
            'users': users
        }

        template = JINJA_ENVIRONMENT.get_template('listUsers.html')
        self.response.write(template.render(template_values))

# [END main_page]


# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/listUsers', ListUsers),
], config=config, debug=True)