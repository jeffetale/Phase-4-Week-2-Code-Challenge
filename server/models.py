from flask_sqlalchemy import SQLAlchemy
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
    description = db.Column(db.String(400), nullable=False)
    created_at = db.Column(db.DateTime, default = datetime.now(nairobi_tz))
    updated_at = db.Column(db.DateTime, default = datetime.now(nairobi_tz), onupdate=datetime.now(nairobi_tz))

    heroes = db.relationship('HeroPower', backref='power', lazy=True)

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.Integer, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)    
    created_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz))
    updated_at = db.Column(db.DateTime, default=datetime.now(nairobi_tz), onupdate=datetime.now(nairobi_tz))





