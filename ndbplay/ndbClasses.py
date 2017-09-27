from google.appengine.ext import ndb


class MyUser(ndb.Model):
    userID = ndb.IntegerProperty(indexed=True)
    firstName = ndb.StringProperty(indexed=False)
    lastName = ndb.StringProperty(indexed=False)
    email = ndb.StringProperty(indexed=False)
    likes = ndb.StringProperty(repeated=True)