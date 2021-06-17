# Tutorial Resources : https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

# Required imports
import os
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app

# 1. Import additional 'storage'
from firebase_admin import storage

# Initialize Flask app
app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('./key.json')

# 2. Initialized firebase app with 'storage' destination specified (omit 'gs://')
default_app = initialize_app(cred, {
    'storageBucket': '[your own storage name].appspot.com'
})


# 3. Create reference to your storage bucket
ds = storage.bucket()



db = firestore.client()
userAccount_ref = db.collection('userAccount')



#4. Try create endpoint for uploading images  (http://localhost:5000/uploadImage)
@app.route('/uploadImage', methods=['GET'])
def uploadImage():
    # 4.1 Specify name of the uploaded file
    uploadContent = ds.blob('image1.png')

    # 4.2 Locate the file
    uploadContent.upload_from_filename(os.path.basename('D:\Work-NECTEC\coding\python-firestore\cat.png'))

    # 4.3 By default, image is not public. In order to get publicly accessible url, we need to specified '.make_public()'
    uploadContent.make_public()

    # 4.4 Return URL for user to access his/her image
    return jsonify({"accessible_url": uploadContent.public_url})




@app.route('/add', methods=['POST'])
def create():
    """        
        ** Send Post Request with Curl command **
        curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Alice\", \"age\":\"20\" }" http://localhost:5000/add
        curl -X POST -H "Content-Type: application/json" -d "{ \"name\": \"Bob\", \"age\":\"25\" }" http://localhost:5000/add
    """
    name = request.json['name']
    userAccount_ref.document(name).set(request.json)
    return jsonify({"success": True})



@app.route('/list', methods=['GET'])
def read():
    """
        ** Try Sending Get Request **

        (Without Query String = list all user accounts)
        curl  http://localhost:5000/list

        (With Query String(name) = list by username)
        curl  http://localhost:5000/list?name=Alice
    """

    # If Check if parameter 'name' was passed to URL query
    username = request.args.get('name')
    if username:
        user = userAccount_ref.document(username).get()
        return jsonify(user.to_dict())

    # If no parameter was passed  ---> loop though user list and return all records
    else:
        all_users = [doc.to_dict() for doc in userAccount_ref.stream()]
        return jsonify(all_users), 200




port = int(os.environ.get('PORT', 8080))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)