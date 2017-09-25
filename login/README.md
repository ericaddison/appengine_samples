# login app

Practice logging in via other web accounts (e.g. Google account).

## google account login
Followed instructions
https://developers.google.com/identity/sign-in/web/sign-in (including create clientID for Oauth)
and here
https://developers.google.com/identity/sign-in/web/backend-auth

### Library hassle!
I went through a lot of trouble trying to get the `google.oauth2` token validation to work, but in the end
I received an error about needing to turn on billing in my account! Here are some of the steps I had to take:
- Create a new directory './lib' in the main app directory
- install "google-auth" and "requests" modules via `pip` into this dir
- (i.e. `sudo pip install -t lib/ google-auth`)
- Add a libraries tag in app.yaml [as explained here](https://cloud.google.com/appengine/docs/standard/python/tools/using-libraries-python-27#vendoring)
- Specify to use the ssl library, [as explained here](https://cloud.google.com/appengine/docs/standard/python/sockets/ssl_support)
- doh! billing error!

So I will just use the endpoint as decribed in the backend-auth link above...