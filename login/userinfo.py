
import webapp2
import urllib
import urllib2
import json
from google.appengine.api import users


class UserInfoHandler(webapp2.RequestHandler):
    def get(self):

        self.response.content_type = 'text/html'
        try:
            user = users.get_current_user()
            self.response.write("<h2>User Info</h2><br><br>")
            if user is None:
                self.response.write("<em>No current user!</em><br>")
            else:
                self.response.write("user ID: " + user.user_id() + "<br>")
                self.response.write("nickname: " + user.nickname() + "<br>")
                self.response.write("email: " + user.email() + "<br>")
            self.response.write("<br><a href='/'>Go Back</a>")
        except Exception, e:
            self.response.write("General error!<br>")
            self.response.write(e)



# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/userinfo', UserInfoHandler),
], debug=True)
