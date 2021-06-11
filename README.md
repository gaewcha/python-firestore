# Connect Flask to Google Firestore

** Study Resource : https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run

#### STEP 1 : Setup Google Firestore Project
1. Setup Google Firestore Project
    1. Go to https://firebase.google.com/products/firestore?gclid=Cj0KCQjw8IaGBhCHARIsAGIRRYrRZ76XGCJPhZgS2-iRHuU2hdNZJFfIe1krpP25c2qx9vAiC5cAdlQaAmiGEALw_wcB&gclsrc=aw.ds
    2. Click on **Visit Console***. Then login with Google Account (gmail)
    3. Click on **+ Add Project**. Once your project is created, enter the project and select **Firestore Database** located on the left panel.
    4. Click **Create Database** and choose **Start in test mode**
    5. On the left panel, select **Project Overview** and choose **Project Setting**
    6. Select **Service Account** tab. Then select **Python** in Admin SDK configuration snippet section.
    7. Click on **Generate new private key** and download JSON file
    8. Rename JSON file to **key.json**

#### STEP 2 : Connect Web Server to Firestore
2. Clone this repository (Assume **Git** was installed on your machine) and replace **key.json** with your own key
```sh
$ git clone https://github.com/gaewcha/python-firestore.git
$ cd python-firestore
```
  requirements:
  - Python3.7
  - Flask
  - Firebase Admin Python SDK  ($ pip install firebase-admin)

3. To run this app
```sh
$ flask run
```
