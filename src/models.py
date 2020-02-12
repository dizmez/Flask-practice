from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Person(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)

#     def __repr__(self):
#         return '<Person %r>' % self.username

#     def serialize(self):
#         return {
#             "username": self.username,
#             "email": self.email
#         }


class Persons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)
   
    


    def __repr__(self):
        return '<Persons %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "password" : self.password
        }

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(256))
   
    


    def __repr__(self):
        return '<Persons %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "password" : self.password
        }


class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    position = db.Column(db.String(50))
    location = db.Column(db.String(50))
    salary = db.Column(db.String(20))

    def __repr__(self):
        return '<Jobs %r>' % self.name

    def serialize(self):
        return {
            "name": self.name,
            "position": self.position,
            "location": self.location,
            "salary": self.salary
        }
