from models import Hero, HeroPower, Power
from app import db,app
import random

with app.app_context():
    db.session.query(HeroPower).delete()
    db.session.query(Power).delete()
    db.session.query(Hero).delete()


    print('\U0001F483 Seeding powers...')

    powers = [ 
    {"name": "super strength", "description": "gives the wielder super-human strength"},
    {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
    {"name": "super human senses", "description": "gives the wielder to use her senses at a super-human level"},
    {"name": "elasticity", "description": "can stretch the human body to extreme lengths"} ]        

    for power in powers:
        p = Power(name = power["name"], 
                description = power["description"])
        db.session.add(p)

        
    print('\U0001F483 Seeding heroes...')

    heroes = [
        {"name": "Kamala Khan", "super_name": "Squirrel Girl"},
        {"name": "Doreen Green", "super_name": "Ms.Marvel"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Max", "super_name": "Scarlet Witch"},
        {"name": "Carol Danver", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Lionel Messi", "super_name": "Goat"},
        {"name": "Ororo Monroe", "super_name": "Storm"},
        {"name": "Elektra Nachois", "super_name": "Elektra"},
    ]

    for hero in heroes:
        h = Hero(name = hero['name'],
                 super_name = hero["super_name"])
        
        db.session.add(h)

    
    print('\U0001F483 Adding powers to heroes...')

    strengths = ["Strong", "Weak", "Average"]
    heroes = Hero.query.all()
    powers = Power.query.all()

    for hero in heroes:
        for n in range(random.randint(1,3)):
            power = random.choice(powers)
            hero_power = HeroPower(hero_id = hero.id,
                                   power_id = power.id,
                                   strength = random.choice(strengths))
            db.session.add(hero_power)

    db.session.commit()
    


    
            
                



