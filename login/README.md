# login app

Practice logging in via other web accounts (e.g. Google account).

https://ea-ut-apt-login.appspot.com/

## google account login with the `users` API
Pretty simple ... used the `users` API to log in.

** There is an interesing difference between this method and the token method... Not sure of the details, BUT, if I
logout with the link you can get from the `users` API, then it logs me out of my other open google sessions in
my browser as well! The token version does not do that, but if you are already logged into something else (say gmail),
then the token version will just grab that and not even give you a choice about which account to use. Odd...

## google account login with a token
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

## Facebook login
Added a Facebook login button after registering a new app as a Facebook developer (https://developers.facebook.com/apps).
Can log in now, but I don't collect the token or anything yet...
Also should take a look at this for a tutorial on how to post with FB: http://nodotcom.org/python-facebook-tutorial.html

## github login
nothing yet...

