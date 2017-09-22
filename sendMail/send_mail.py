
from google.appengine.api import app_identity
from google.appengine.api import mail
from google.appengine.runtime import apiproxy_errors
import webapp2


# send an email with the send_mail method
def send_mail(from_address, to_address, subject, body):
    mail.send_mail(sender=from_address,
                   to=to_address,
                   subject=subject,
                   body=body)


# send an email with the EmailMessage class
def send_mail_class(from_address, to_address, subject, body):
    message = mail.EmailMessage()
    message.sender = from_address
    message.to = to_address
    message.subject = subject
    message.body = body
    message.send()


class SendMailHandler(webapp2.RequestHandler):
    def post(self):
        try:
            # gather variables from the POST request
            from_address = 'emailer_dude@{}.appspotmail.com'.format(
                app_identity.get_application_id())
            to_address = self.request.get('to_address')
            subject = self.request.get('subject')
            body = self.request.get('body')
            send_method = self.request.get('send_style')

            self.response.content_type = 'text/html'

            # Send the email
            if send_method == "method":
                send_mail(from_address, to_address, subject, body)
            elif send_method == "class":
                send_mail_class(from_address, to_address, subject, body)
            else:
                self.response.write('Invalid email method')
                return

            # write out the details to the page
            self.response.write('Email details:<br><br>')
            self.response.write('From: ' + from_address + '<br><br>')
            self.response.write('To: ' + to_address + '<br><br>')
            self.response.write('Subject: ' + subject + '<br><br>')
            self.response.write('Body: ' + body + '<br><br><br><br>')
            self.response.write('Send method: ' + send_method + '<br><br>')
            self.response.write('<a href="/">Go Back</a>')
        except apiproxy_errors.OverQuotaError, e:
            self.response.content_type = 'text/html'
            self.response.write("App has exceeded some quota!!<br><br>")
            self.response.write(e)


# define the "app" that will be referenced from app.yaml
# which pairs the resouce '/send_mail' with the class SendMailHandler
app = webapp2.WSGIApplication([
    ('/send_mail', SendMailHandler),
], debug=True)
