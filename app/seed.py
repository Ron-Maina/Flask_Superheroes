#!/usr/bin/env python3

from models import Powers, Heroes, HeroPowers, db
from app import app
from random import randint, choice as rc, sample


with app.app_context():
  
  HeroPowers.query.delete()
  Powers.query.delete()
  Heroes.query.delete()

  heroes = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }
  ]
  heroes_list = []
  for hero in heroes:
    instance = Heroes(
      name = hero['name'],
      super_name = hero['super_name']
    )
    heroes_list.append(instance)

  db.session.add_all(heroes_list)
  db.session.commit()
  print('SEEDED HEROES.....')


  powers = [
    { "name": "super strength", "description": "gives the wielder super-human strengths" },
    { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
    { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
    { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
  ]
  powers_list = []
  for power in powers:
    instance = Powers(
      name = power['name'],
      description = power['description']
    )
    powers_list.append(instance)

  db.session.add_all(powers_list)
  db.session.commit()
  print('SEEDED POWERS.....')



  strengths = ["Strong", "Weak", "Average"]
  for hero in heroes_list:
    list = sample([power.id for power in powers_list], randint(1,4))
    for i in list:
      instance = HeroPowers(
        strength = rc(strengths),
        hero_id = hero.id,
        power_id = i
      )
      db.session.add(instance)
      db.session.commit()

  print('SEEDED HERO_POWERS......')
