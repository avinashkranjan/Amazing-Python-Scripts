import pyrebase

import FirebaseScripts.CredentialsHelper as credentials

firebase = pyrebase.initialize_app(credentials.get_fireBase_credentials())

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
    response = storage.child(firebase_path).download(
        path="./", filename=file_name)
    print(response)
    return response


if __name__ == "__main__":
    download_file("enter your path here ", "enter your file name here ")
