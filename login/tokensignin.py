import urllib
import urllib2
import webapp2
import json
from google.appengine.api import users


# [START main_page]
class TokenSignIn(webapp2.RequestHandler):

    def post(self):
        token = str(self.request.POST['idtoken'])
        user_data_str = urllib2.urlopen('https://www.googleapis.com/oauth2/v3/tokeninfo?id_token='+token).read()
        user_data = json.loads(user_data_str)

        self.response.content_type = 'text/html'
        self.response.write(user_data['name'])

# [END main_page]

# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/tokensignin', TokenSignIn),
], debug=True)