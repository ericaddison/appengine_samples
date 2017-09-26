import urllib
import webapp2
from BaseHandler import BaseHandler
from BaseHandler import config


# [START main_page]
class LoginPage(BaseHandler):
    def get(self):
        self.response.content_type = 'text/html'
        self.response.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="google-signin-scope" content="profile email">
    <meta name="google-signin-client_id" content="507403931896-csnvbghp9ijpdhrf3hkag7np61aejmr5.apps.googleusercontent.com">
    <script src="https://apis.google.com/js/platform.js" async defer></script>
    <title>Google Login Practice</title>
</head>
<body>
<center>
<h1>Welcome to my App!</h1>
<h2 id="banner">Please log in with your google account :)</h2>
    <div id="logins">
    <div class="g-signin2" data-onsuccess="onSignIn" data-theme="dark"></div>
    </div>
    <script>
      function onSignIn(googleUser) {
        // Useful data for your client-side scripts:
        // The ID token you need to pass to your backend:
        var id_token = googleUser.getAuthResponse().id_token;
        console.log("ID Token: " + id_token);
        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/tokensignin');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
          document.getElementById("banner").innerHTML = "Hello, " + xhr.responseText
        };
        xhr.send('idtoken=' + id_token);
      };
    </script>
<a href="#" onclick="signOut();">Sign out</a>
<script>
  function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
      var xhr = new XMLHttpRequest();
        xhr.open('POST', '/signout');
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.send();
    });
    document.getElementById("banner").innerHTML = "Please log in with your google account :)"
  }
</script>
<br><br>
<a href="/anotherPage">check session ID</a>
</body>
</html>""")
# [END main_page]

# define the "app" that will be referenced from app.yaml
app = webapp2.WSGIApplication([
    ('/', LoginPage),
], config=config, debug=True)