
from google.appengine.api import app_identity
from google.oauth2 import id_token
from google.auth.transport import requests
import webapp2
import urllib
import json

CLIENT_ID = "507403931896-csnvbghp9ijpdhrf3hkag7np61aejmr5.apps.googleusercontent.com"

def verify_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), CLIENT_ID)

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('Wrong issuer.')

        # ID token is valid. Get the user's Google Account ID from the decoded token.
        return idinfo
    except ValueError:
        # Invalid token
        return None


class SigninHandler(webapp2.RequestHandler):
    def post(self):
        appName = app_identity.get_application_id()
        token = str(self.request.POST['idtoken'])

        self.response.content_type = 'text/html'
        try:
            idinfo = verify_google_token(token)
            if idinfo is None:
                self.response.write("No idinfo!<br>")
            self.response.write(str(idinfo.keys))
        except Exception, e:
            self.response.write("General error!<br>")
            self.response.write(e)



# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/tokensignin', SigninHandler),
], debug=True)
