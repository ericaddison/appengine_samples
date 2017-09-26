import urllib2
import webapp2
import json
from BaseHandler import BaseHandler
from BaseHandler import config
from random import randint

# [START main_page]
class TokenSignIn(BaseHandler):

    def post(self):
        token = str(self.request.POST['idtoken'])
        user_data_str = urllib2.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token).read()
        user_data = json.loads(user_data_str)

        # set a session ID
        self.session['signedIn'] = True
        # sub = subject = userID
        self.session['userID'] = user_data['sub']

        self.response.content_type = 'text/html'
        self.response.write(user_data['name'])

class SignOut(BaseHandler):
    def post(self):
        # set a session ID
        self.session['signedIn'] = False
# [END main_page]

# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/tokensignin', TokenSignIn),
    ('/signout', SignOut)
], config=config, debug=True)