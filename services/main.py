
from google.appengine.api import urlfetch
from google.appengine.api import app_identity
import webapp2
import urllib
import json


class MainHandler(webapp2.RequestHandler):
    def get(self):
        appName = app_identity.get_application_id()
        self.response.content_type = 'text/html'
        try:
            # create an rpc object from urlfetch
            rpc = urlfetch.create_rpc()

            # build the url used to call the service
            # including the GET parameters sent with this request
            url = 'https://service1.' + appName + '.appspot.com?' + urllib.urlencode(self.request.GET)

            # make the service call
            urlfetch.make_fetch_call(rpc, url)
            response = rpc.get_result()

            # write out some info
            self.response.write("status code: " + str(response.status_code) + "<br>")
            self.response.write("content: " + response.content + "<br><br>")

            # store response as dictionary
            data = json.loads(response.content)
            for key in data:
                self.response.write(key + ": " + data[key] + "<br>")

            # return link
            self.response.write("<br><a href='/'>Go Back</a>")

        except urlfetch.DownloadError, e:
            self.response.write("Download error!<br>")
            self.response.write(e)
        except Exception, e:
            self.response.write("General error!<br>")
            self.response.write(e)


# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/call_service1', MainHandler),
], debug=True)
