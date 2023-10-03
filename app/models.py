from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates


metadata = MetaData(naming_convention={
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
})

db = SQLAlchemy(metadata=metadata)

class Heroes(db.Model, SerializerMixin):
    __tablename__ = 'heroes'

    serialize_rules = ('-hero_powers.hero', '-created_at', '-updated_at', 
                       '-hero_powers.hero_id', '-hero_powers.id', 
                       '-hero_powers.power_id', '-hero_powers.strength')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    super_name = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.Relationship('HeroPowers', backref= 'hero')


class Powers(db.Model, SerializerMixin):
    __tablename__ = 'powers'

    serialize_rules = ('-hero_powers.power', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable = False)
    description = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_powers = db.Relationship('HeroPowers', backref= 'power')

    @validates('description')
    def validate_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be atleast 20 characters long")
        return description    


class HeroPowers(db.Model, SerializerMixin):
    __tablename__ = 'hero_powers'

    serialize_rules = ('-hero.hero_powers', '-power.hero_powers', '-created_at', '-updated_at')

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable = False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable = False)

    @validates('strength')
    def validates_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be Strong, Weak, or Average")
        return strength

