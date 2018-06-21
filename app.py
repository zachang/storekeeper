from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': 'Shoppy',
        'items': [
            {
                'name': 'Bread',
                'price': 3.00
            },
            {
                'name': 'Biscuits',
                'price': 10.00
            },
        ]
    }
]

@app.route('/store', methods=['POST'])
def add_store():
    pass


@app.route('/store/<string:name>/item', methods=['POST'])
def add_store_item(name):
    pass


@app.route('/store')
def retrieve_stores():
    return jsonify({'store': stores})


@app.route('/store/<string:name>')
def retrieve_store(name):
    pass


@app.route('/store/<string:name>/item')
def retrieve_store_items(name):
    pass



if __name__ == '__main__':
    app.run(port=3000,debug=True)