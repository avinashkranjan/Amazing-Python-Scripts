import pyrebase

import FirebaseScripts.CredentialsHelper as credentials

firebase = pyrebase.initialize_app(credentials.get_fireBase_credentials())

database = firebase.database()


def create_data_path():
    response = database.child("testdata")
    print(response)
    return response


def add_data(data):
    response = database.child("testdata").push(data)
    print(response)
    return response


def set_key_of_data(data):
    response = database.child("testdata").child("newKey").set(data)
    print(response)
    return response


def update_data(updateData):
    response = database.child("testdata").child("newKey").update(updateData)
    print(response)
    return response


def delete_data(key):
    response = database.child("testdata").child(key).remove()
    print(response)
    return response


def retrieve_data():
    response = database.child("testdata").get()
    print("data " + str(response))
    print("Keys : " + str(response.key()))
    print("Values : " + str(response.val()))
    return response


def print_all_data():
    for i in retrieve_data().each():
        print(i.key())
        print(i.val())


if __name__ == "__main__":
    print_all_data()
