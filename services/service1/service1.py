
from google.appengine.api import app_identity
import json
import webapp2
import re


def service_function(v1, v2):
    return v1+v2


class Service1Handler(webapp2.RequestHandler):
    def get(self):
        # gather variables from the GET request
        s1 = cleanhtml(self.request.get('string1'))
        s2 = cleanhtml(self.request.get('string2'))

        out = {'string1': s1,
               'string2': s2,
               'concatenation': service_function(s1, s2),
               'app': app_identity.get_application_id()}

        self.response.content_type = 'text/html'
        self.response.write(json.dumps(out))


def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

# define the "app" that will be referenced from app.yaml
service = webapp2.WSGIApplication([
    ('/', Service1Handler),
], debug=True)
