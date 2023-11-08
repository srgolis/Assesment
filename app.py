from flask import Flask, request, jsonify

app = Flask(__name__)
# Sample data - you might use a database in a real application
data = []

# Create
@app.route('/items', methods=['POST'])
def create_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201

# Read
@app.route('/items', methods=['GET'])
def get_all_items():
    return jsonify(data)

# Update
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    for item in data:
        if item.get('id') == item_id:
            item.update(request.json)
            return jsonify(item), 200
    return "Item not found", 404

# Delete
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    for index, item in enumerate(data):
        if item.get('id') == item_id:
            del data[index]
            return "Item deleted", 200
    return "Item not found", 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
