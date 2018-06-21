from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'Shoppy',
        'items': [
            {
                'name': 'Bread',
                'price': 3.00
            }
        ]
    }
]

@app.route('/')
def index():
    return 'Welcome to store'

@app.route('/store', methods=['POST'])
def add_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }

    stores.append(new_store)
    return jsonify(stores)


@app.route('/store/<string:name>/item', methods=['PUT'])
def add_store_item(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
        return jsonify({'message': 'store not found'})
    

@app.route('/store')
def retrieve_stores():
    return jsonify({'store': stores})


@app.route('/store/<string:name>')
def retrieve_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})


@app.route('/store/<string:name>/item')
def retrieve_store_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})



if __name__ == '__main__':
    app.run(port=3000,debug=True)