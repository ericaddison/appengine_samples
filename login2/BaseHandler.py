import webapp2

from webapp2_extras import sessions

class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        # Get a session store for this request.
        self.session_store = sessions.get_store(request=self.request)
        try:
            # Dispatch the request.
            webapp2.RequestHandler.dispatch(self)
        finally:
            # Save all sessions.
            self.session_store.save_sessions(self.response)

    @webapp2.cached_property
    def session(self):
        # Returns a session using the default cookie key.
        sess = self.session_store.get_session()
        #add some default values:
        if not sess.get('theme'):
            sess['theme']='cosmo'
        return sess

config = {}
config['webapp2_extras.sessions'] = {
    'secret_key': 'my-super-secret-key',
}