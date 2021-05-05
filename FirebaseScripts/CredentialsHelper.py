import os

from dotenv import load_dotenv

dotenv_path = "./credentials.env"
load_dotenv(dotenv_path)

firebaseConfig = {
    "apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}


def get_fireBase_credentials():
    try:

        # Accessing variables.

        apiKey = os.getenv('apiKey')
        authDomain = os.getenv('authDomain')
        databaseURL = os.getenv('databaseURL')
        projectId = os.getenv('projectId')
        storageBucket = os.getenv('storageBucket')
        messagingSenderId = os.getenv('messagingSenderId')
        appId = os.getenv('appId')
        measurementId = os.getenv('measurementId')
        credentials = [apiKey, authDomain, databaseURL, projectId, storageBucket, messagingSenderId, appId,
                       measurementId]
        if any(not(credential) for credential in credentials):
            raise ValueError("Value cannot be None ")
        else:
            firebaseConfig["apiKey"] = apiKey
            firebaseConfig["authDomain"] = authDomain
            firebaseConfig["databaseURL"] = databaseURL
            firebaseConfig["projectId"] = projectId
            firebaseConfig["storageBucket"] = storageBucket
            firebaseConfig["messagingSenderId"] = messagingSenderId
            firebaseConfig["appId"] = appId
            firebaseConfig["measurementId"] = measurementId

    except:
        print("error while getting the Keys ")
        raise

    return firebaseConfig

get_fireBase_credentials()