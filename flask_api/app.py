from flask import Flask, request
import user_service

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

@app.get('/user')
def get_all_user():
    return user_service.get_all()

@app.get('/user/<userId>')
def get_user(userId):
    return user_service.get_user_by_id(userId)

@app.post('/user/new')
def create_user():
    body = request.get_json()
    print("check")
    createUserData = {
        'name': body['name'],
        'age': int(body['age'])
    }
    user_service.create_user(createUserData)
    return "success"

@app.put('/user/<userId>')
def update_user(userId):
    body = request.get_json()

    updateUserData = {
        'name': body['name'],
        'age': int(body['age'])
    }
    user_service.update_user(userId, updateUserData)
    return "success"

@app.delete('/user/<userId>')
def delete_user(userId):
    user_service.delete_user(userId)
    return "success"

if __name__ == '__main__':
    app.run(debug=True)
