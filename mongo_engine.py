from flask import Flask,request, jsonify
from flask_mongoengine import MongoEngine
from healthcheck import HealthCheck
import json

app = Flask(__name__)

health = HealthCheck()

app.config['MONGODB_SETTINGS'] = {
    'db': 'Devops',
    'host': 'localhost',
    'port': 27017
}

db = MongoEngine()
db.init_app(app)

class task1(db.Document):
    name = db.StringField()
    age = db.IntField()
    sub = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "age": self.age,
                "sub" : self.sub}

@app.route("/")
def root_path():
    return("welcome")


@app.route('/user/', methods=['GET'])
def get_user():
    contact = task1.objects()
    if not contact:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(contact) 


@app.route('/user/', methods=['POST'])
def add_user():
    record = json.loads(request.data)
    contact = task1(name=record['name'],
                age=record['age'],
                sub=record['sub'])
    contact.save()
    return jsonify(contact)  


@app.route('/user/<id>', methods=['PUT'])
def Update_user(id):
    record = json.loads(request.data)
    contact = task1.objects.get_or_404(id=id)
    if not contact:
        return jsonify({'error': 'data not found'})
    else:
        contact.update(name=record['name'],
                    age=record['age'],
                    sub=record["sub"])
    return jsonify(contact) 



@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    contact = task1.objects(id=id)
    if not contact:
        return jsonify({'error': 'data not found'})
    else:
        contact.delete()
    return jsonify(contact)


#Table2
class cars(db.Document):
    name = db.StringField()
    model = db.StringField()
    price = db.StringField()
    def to_json(self):
        return {"name": self.name,
                "model": self.model,
                "price" : self.price}  

@app.route('/model/', methods=['GET'])
def get_model():
    product = cars.objects()
    if not product:
        return jsonify({'error': 'data not found'})
    else:
        return jsonify(product)



@app.route('/model/', methods=['POST'])
def add_model():
    record = json.loads(request.data)
    product = cars(name=record['name'],
                model=record['model'],
                price=record['price'])
    product.save()
    return jsonify(product)



@app.route('/model/<id>', methods=['PUT'])
def Update_model(id):
    record = json.loads(request.data)
    product = cars.objects.get_or_404(id=id)
    if not product:
        return jsonify({'error': 'data not found'})
    else:
        product.update(name=record['name'],
                    model=record['model'],
                    price=record['price'])
        # product.save()
    return jsonify(product)


@app.route('/model/<id>', methods=['DELETE'])
def delete_model(id):
    product = cars.objects(id=id)
    if not product:
        return jsonify({'error': 'data not found'})
    else:
        product.delete()
    return jsonify(product)                 











