
from google.appengine.api import app_identity
import json
import webapp2


def service_function(v1, v2):
    return v1+v2


class Service1Handler(webapp2.RequestHandler):
    def get(self):
        # gather variables from the GET request
        v1 = self.request.get('var1')
        v2 = self.request.get('var2')

        out = {'v1': v1,
               'v2': v2,
               'result': service_function(v1, v2),
               'app': app_identity.get_application_id()}

        self.response.content_type = 'text/html'
        self.response.write(json.dumps(out))

# define the "app" that will be referenced from app.yaml
service = webapp2.WSGIApplication([
    ('/', Service1Handler),
], debug=True)
