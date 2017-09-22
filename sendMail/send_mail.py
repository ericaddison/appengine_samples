
from google.appengine.api import app_identity
from google.appengine.api import mail
import webapp2


# send an email
def send_mail(from_address, to_address, subject, body):
    mail.send_mail(sender=from_address,
                   to=to_address,
                   subject=subject,
                   body=body)


class SendMailHandler(webapp2.RequestHandler):
    def post(self):

        send_mail('{}@appspot.gserviceaccount.com'.format(
            app_identity.get_application_id()))
        self.response.content_type = 'text/plain'
        self.response.write('Sent an email to Albert.')


app = webapp2.WSGIApplication([
    ('/send_mail', SendMailHandler),
], debug=True)
