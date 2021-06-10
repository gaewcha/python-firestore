# Tutorial Resources : https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('./key.json')
default_app = initialize_app(cred)
db = firestore.client()
userAccount_ref = db.collection('userAccount')

@app.route('/add', methods=['POST'])
def create():
    """        
        ** Send Post Request with Curl command **
        curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Alice\", \"age\":\"20\" }" http://localhost:5000/add
        curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Bob\", \"age\":\"25\" }" http://localhost:5000/add
    """
    try:
        name = request.json['name']
        userAccount_ref.document(name).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"



@app.route('/list', methods=['GET'])
def read():
    """
        ** Try Sending Get Request **

        (Without Query String = list all user accounts)
        curl  http://localhost:5000/list

        (With Query String(name) = list by username)
        curl  http://localhost:5000/list?name=Alice
    """
    try:
        # If Check if parameter 'name' was passed to URL query
        username = request.args.get('name')
        if username:
            user = userAccount_ref.document(username).get()
            return jsonify(user.to_dict())

        # If no parameter was passed  ---> loop though user list and return all records
        else:
            all_users = [doc.to_dict() for doc in userAccount_ref.stream()]
            return jsonify(all_users), 200

    except Exception as e:
        return f"An Error Occured: {e}"



port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)