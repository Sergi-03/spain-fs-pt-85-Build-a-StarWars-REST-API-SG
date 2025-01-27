from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorites = relationship("Favorite", back_populates="user")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "favorites": [favorite.serialize() for favorite in self.favorites]  
        }

class Character(db.Model):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(500), nullable=False)
    favorites = relationship("Favorite", back_populates="character")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

class Planet(db.Model):
    __tablename__ = 'planet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(150),  nullable=False)
    description = Column(String(500), nullable=False)
    favorites = relationship("Favorite", back_populates="planet")


    def serialize(self):
        return {
            "id": self.id,
            "planet_name": self.planet_name,
            "description": self.description
        }

class Favorite(db.Model):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")



    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character": self.character.name if self.character else None,
            "planet": self.planet.planet_name if self.planet else None
        }

    def __repr__(self):
        return '<User %r>' % self.username

    


# from flask_sqlalchemy import SQLAlchemy

# db = SQLAlchemy()

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), unique=False, nullable=False)
#     is_active = db.Column(db.Boolean(), unique=False, nullable=False)

#     def __repr__(self):
#         return '<User %r>' % self.username

#     def serialize(self):
#         return {
#             "id": self.id,
#             "email": self.email,
#             # do not serialize the password, its a security breach
#         }