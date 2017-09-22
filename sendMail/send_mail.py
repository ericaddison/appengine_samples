
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

        # gather variables from the POST request
        from_address = '{}@appspot.gserviceaccount.com'.format(
            app_identity.get_application_id())
        to_address = self.request.get('to_address')
        subject = self.request.get('subject')
        body = self.request.get('body')

        # Send the email
        send_mail(from_address, to_address, subject, body)

        # write out the details to the page
        self.response.content_type = 'text/html'
        self.response.write('Email details:')
        self.response.write('From: ' + from_address + '<br><br>')
        self.response.write('To: ' + to_address + '<br><br>')
        self.response.write('Subject: ' + subject + '<br><br>')
        self.response.write('Body: ' + body + '<br><br>')


# define the "app" that will be referenced from app.yaml
# which pairs the resouce '/send_mail' with the class SendMailHandler
app = webapp2.WSGIApplication([
    ('/send_mail', SendMailHandler),
], debug=True)
