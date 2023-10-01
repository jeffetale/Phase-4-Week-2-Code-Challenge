#!/usr/bin/env python3
from flask import Flask, jsonify
from flask_migrate import Migrate
from models import db, Hero, HeroPower, Power

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route("/")
def home():
    return "Hello"

@app.route("/heroes", methods=["GET"])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]), 200

@app.route("/heroes/<int:id>", methods=["GET"])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero is None:
        return jsonify({"error": "Hero not found"}), 404

    powers = []
    for hero_power in hero.powers:
        power = hero_power.power
        powers.append({
            "id": power.id,
            "name": power.name,
            "description": power.description
        })

    return jsonify({
        "id": hero.id,
        "name": hero.name,
        "super_name": hero.super_name,
        "powers": powers
    }), 200

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([{"id": power.id, "name": power.name, "description": power.description} for power in powers]), 200

@app.route("/powers/<int:id>", methods=["GET"])
def get_power(id):
    power = Power.query.get(id)
    if power is None:
        return jsonify({"error": "Power not found"}), 404
    
    return jsonify({"id" : power.id, "name": power.name, "description": power.description}), 200
           


if __name__ == "__main__":
    app.run(port=5555)
