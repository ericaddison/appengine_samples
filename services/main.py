
from google.appengine.api import urlfetch
from google.appengine.api import app_identity
import webapp2
import urllib



class MainHandler(webapp2.RequestHandler):
    def get(self):
        appName = app_identity.get_application_id()
        self.response.content_type = 'text/html'
        try:
            rpc = urlfetch.create_rpc()

            # HOW TO ADD PARAMS TO THE CALL???
            url = 'https://service1.' + appName + '.appspot.com?' + urllib.urlencode(self.request.GET)
            urlfetch.make_fetch_call(rpc, url)

            response = rpc.get_result()
            self.response.write("status code: " + str(response.status_code) + "<br>")
            self.response.write("content: " + response.content + "<br>")
            self.response.write("<br><a href='/'>Go Back</a>")

        except urlfetch.DownloadError:
            self.response.write("Error!!!")
        except Exception, e:
            print e


# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/call_service1', MainHandler),
], debug=True)
