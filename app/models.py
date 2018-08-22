from app import db
from datetime import datetime
from flask.ext.login import UserMixin

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))
    email = db.Column(db.String(50))
    author = db.relationship('Post',backref='author',lazy='dynamic')
    
    
    def __str__(self):
                return self.username
    
    __repr__=__str__

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key=True)    
    create_time = db.Column(db.DateTime,default=datetime.now)
    title = db.Column(db.String(70))
    post = db.Column(db.Text)
    author_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    
        
    def __str__(self):
                return self.title
    __repr__=__str__ 
    
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key=True)
    content = db.Column(db.Text)
    create_time = db.Column(db.DateTime,default=datetime.now)
    name_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    name = db.relationship('User',backref=db.backref('comments',lazy='dynamic')) 
    post_id = db.Column(db.Integer)    
    def __str__(self):
                return self.content 
    __repr__=__str__
