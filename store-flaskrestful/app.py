from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity
from security import authenticate, identity

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcde'
api = Api(app)

jwt = JWT(app, authenticate, identity)

items = []

class Items(Resource):
    """Items resource"""
    @jwt_required()
    def get(self, name):
        item = next(filter(lambda stock: stock['name'] == name, items), None)
        return {'item': item}, 200 if item else 404

    def post(self, name):
        if next(filter(lambda stock: stock['name'] == name, items), None) is not None:
            return {'message': 'Item already exist'}, 400
        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return items, 201

    def delete(self, name):
        global items
        items = list(filter(lambda stock: stock['name'] != name, items))
        return {"message": "Item deleted"}

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("price",
            type=float,
            required=True,
            help="This field cannot be left blank!"
        )
        data = parser.parse_args()
        item = next(filter(lambda stock: stock['name'] == name, items), None)
        if item is None:
            item = {"name": name, "price": data["price"]}
            items.append(item)
        else:
            item.update(data)
        return item


class ItemList(Resource):

    def get(cls):
        return {'items': items}



api.add_resource(Items, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(debug=True, port=3000)