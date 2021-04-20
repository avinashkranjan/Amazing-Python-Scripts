import pyrebase

from FirebaseScripts import CredentialsHelper

firebase = pyrebase.initialize_app(CredentialsHelper.firebaseConfig)

storage = firebase.storage()


def send_file(firebase_path, source_path):
    response = storage.child(firebase_path).put(source_path)
    print(response)
    return response


def delete_file(firebase_path, name_of_file_to_delete):
    response = storage.child(firebase_path).delete(name_of_file_to_delete)
    print(response)
    return response


def download_file(firebase_path, file_name):
    response = storage.child(firebase_path).download(path="./", filename=file_name)
    print(response)
    return response
