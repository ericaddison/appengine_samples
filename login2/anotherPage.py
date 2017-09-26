import urllib
import webapp2
from BaseHandler import BaseHandler
from BaseHandler import config


# [START main_page]
class AnotherPage(BaseHandler):
    def get(self):

        self.response.content_type = 'text/html'
        if self.session['signedIn']:
            self.response.write("UserID = " + str(self.session['userID']))
        else:
            self.response.write("Please <a href='/'>sign in</a> to continue")
# [END main_page]

# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/anotherPage', AnotherPage),
], config=config, debug=True)