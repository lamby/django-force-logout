README
======

 * Add django_force_logout.middleware.ForceLogoutMiddleware to middleware

 * Setup FORCE_LOGOUT_CALLBACK in your settings to point to a method which,
   given a User, will return a nullable timestamp for that user.

   This would typically be stored on custom User model or some other field
   depending on your setup.

   For example::

       def force_logout_callback(user):
           return user.some_profile_model.force_logout

   Alternatively, you can just specify a lambda directly::

       FORCE_LOGOUT_CALLBACK = lambda x: x.some_profile_model.force_logout

 * To forcibly log that user out, set that timestamp field to the current time.
