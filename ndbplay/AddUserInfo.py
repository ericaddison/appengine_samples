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
class AddUserInfo(BaseHandler):
    def post(self):

        fname = self.request.POST['fname']
        lname = self.request.POST['lname']
        email = self.request.POST['email']
        likes = self.request.POST['likes']
        like_list = likes.split(', ')

        new_user = MyUser(firstName=fname, lastName=lname, email=email, likes=like_list, id=email)
        user_key = new_user.put()

        # these are the values that will be fed into the Jinja2 HTML template
        template_values = {
            'title': "Added user " + str(fname),
            'user_key': user_key,
            'user': new_user
        }

        template = JINJA_ENVIRONMENT.get_template('addUser.html')
        self.response.write(template.render(template_values))

# [END main_page]


# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/addUserInfo', AddUserInfo),
], config=config, debug=True)