from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
# Tabla intermedia para la relación muchos a muchos entre usuarios y planetas favoritos
favorite_planets = db.Table(
    'favorite_planets',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('planet_id', db.Integer, db.ForeignKey('planet.id'), primary_key=True)
)
# Tabla intermedia para la relación muchos a muchos entre usuarios y personajes favoritos
favorite_people = db.Table(
    'favorite_people',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('people_id', db.Integer, db.ForeignKey('people.id'), primary_key=True)
)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean, nullable=False, default=True)
    favorite_planets = db.relationship('Planet', secondary=favorite_planets, backref=db.backref('favorited_by_users', lazy='dynamic'))
    favorite_people = db.relationship('People', secondary=favorite_people, backref=db.backref('favorited_by_users', lazy='dynamic'))
    def __repr__(self):
        return '<User %r>' % self.email
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            "favorite_planets": [planet.serialize() for planet in self.favorite_planets],
            "favorite_people": [person.serialize() for person in self.favorite_people]
        }
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    height = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<People %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "eye_color": self.eye_color,
            "height": self.height,
        }
class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    population = db.Column(db.String(250), nullable=False)
    def __repr__(self):
        return '<Planet %r>' % self.name
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "climate": self.climate,
            "population": self.population,
        }
