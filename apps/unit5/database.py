from google.appengine.ext import db

class Users(db.Model):
	username = db.StringProperty(required=True)
	salt = db.StringProperty(required=True)
	password = db.StringProperty(required=True)
	email = db.StringProperty(required=False)

class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.StringProperty(required=True, multiline=True)
    created = db.DateTimeProperty(auto_now_add=True)