from flask import Flask, request, jsonify
import user_service

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.get('/user')
def get_all_user():
    status,result = user_service.get_all()
    return jsonify(result), status

@app.get('/user/<userId>')
def get_user(userId):
    status,result = user_service.get_user_by_id(userId)
    return jsonify(result), status

@app.post('/user/new')
def create_user():
    body = request.get_json()
    createUserData = {
        'name': body['name'],
        'age': int(body['age'])
    }
    status,result = user_service.create_user(createUserData)
    return jsonify(result), status

@app.put('/user/<userId>')
def update_user(userId):
    body = request.get_json()

    updateUserData = {
        'name': body['name'],
        'age': int(body['age'])
    }
    status,result = user_service.update_user(userId, updateUserData)
    return jsonify(result), status

@app.delete('/user/<userId>')
def delete_user(userId):
    status,result = user_service.delete_user(userId)
    return jsonify(result), status

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
