from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from datetime import datetime
import pytz

db = SQLAlchemy()
nairobi_tz = pytz.timezone('Africa/Nairobi')

class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz))
    updated_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz), onupdate=datetime.now(nairobi_tz))

    powers = db.relationship('HeroPower', backref='hero', lazy=True)

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(20), nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.now(nairobi_tz))
    updated_at = db.Column(db.DateTime, default = datetime.now(nairobi_tz), onupdate=datetime.now(nairobi_tz))

    heroes = db.relationship('HeroPower', backref='power', lazy=True)

    @validates('description')
    def validate_description(self, key, description):
        assert len(description) >= 20 , "Description must be present and at least 20 characters long"

        return description

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(100), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz))
    updated_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz), onupdate=datetime.now(nairobi_tz))

    @validates('strength')
    def validate_strength(self, key, strength):
        assert strength in ['Strong', 'Weak', 'Average'], 'strength must be either: Strong, Average or Weak'

        return strength
    
