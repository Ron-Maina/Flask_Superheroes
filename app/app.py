#!/usr/bin/env python3
from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.exceptions import BadRequest
import os

from models import db, Heroes, Powers, HeroPowers

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

api = Api(app)

class Index(Resource):
    def get(self):
        response_dict = {
            "message": "Welcome to the Superheroes Api"
        }
        response = make_response(
            jsonify(response_dict),
            200
        )
        return response
api.add_resource(Index, '/')

class Hero(Resource):
    def get(self):
        heroes_list = []
        for hero in Heroes.query.all():
            hero_dict = {
                "id": hero.id,
                "name": hero.name,
                "super_name": hero.super_name
            }
            heroes_list.append(hero_dict)
        
        response = make_response(
            jsonify(heroes_list),
            200
        )
        return response
        

api.add_resource(Hero, '/heroes')

class HeroesByID(Resource):
    def get(self, id):
        hero = Heroes.query.filter_by(id=id).first()
        if hero is None:
            return {'error': 'Hero not found'}, 404
        
        hero_dict = {
            'id': hero.id,
            'name': hero.name,
            'super_name': hero.super_name,
            'powers': [{"id":hero_power.power.id,"name": hero_power.power.name, "description": hero_power.power.description} 
                       for hero_power in hero.hero_powers]
        }
        response = make_response(
            jsonify(hero_dict),
            200
        )
        return response

api.add_resource(HeroesByID, '/heroes/<int:id>')

class Power(Resource):
    def get(self):
        powers_list = []
        for power in Powers.query.all():
            power_dict = {
                'id': power.id,
                'name': power.name,
                'description': power.description
            }
            powers_list.append(power_dict)

        response = make_response(
            jsonify(powers_list),
            200
        )
        return response
    
api.add_resource(Power, '/powers')

class PowerByID(Resource):
    def get(self, id):
        power = Powers.query.filter_by(id=id).first()
        if power is None:
            return {'error': 'Power not found'}, 404
        power_dict = {
            'id': power.id,
            'name': power.name,
            'description': power.description
        }
        response = make_response(
            jsonify(power_dict),
            200
        )
        return response
    
    def patch(self, id):
        try:
            power = Powers.query.filter_by(id=id).first()
            if power is None:
                return {'error': 'Power not found'}, 404
            else:
                for attr in request.form:
                    setattr(power, attr, request.form.get(attr))
            
            db.session.add(power)
            db.session.commit()

            power_dict = {
                'id': power.id,
                'name': power.name,
                'description': power.description
            }
            response = make_response(
                jsonify(power_dict),
                200
            )
            return response
        except ValueError:
            raise BadRequest(["validation errors"])
               
api.add_resource(PowerByID, '/powers/<int:id>')

class HeroPower(Resource):
    def post(self):
        try:
            new_hero_power = HeroPowers(
                strength =request.form['strength'],
                hero_id = request.form['hero_id'],
                power_id = request.form['power_id']
            )
            db.session.add(new_hero_power)
            db.session.commit()
            powers = [
                {
                    "id": hero_power.power.id,
                    "name": hero_power.power.name,
                    "description": hero_power.power.description
                } for hero_power in HeroPowers.query.filter_by(hero_id=new_hero_power.hero.id).all()
            ]
            new_dict = {
                'id': new_hero_power.hero.id,
                'name': new_hero_power.hero.name,
                'super_name': new_hero_power.hero.super_name,
                'powers': powers
            }
            response = make_response(
                jsonify(new_dict),
                200
            )
            return response
        
        except ValueError:
            raise BadRequest(["validation errors"])


api.add_resource(HeroPower, '/hero_powers')

if __name__ == '__main__':
    app.run(port=5555)
