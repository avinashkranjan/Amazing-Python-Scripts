import pyrebase

import FirebaseScripts.CredentialsHelper as credentials

firebase = pyrebase.initialize_app(credentials.get_fireBase_credentials())

auth = firebase.auth()


def create_user_with_token():
    token = auth.create_custom_token("enter the token here ")
    print(token)
    return token


def create_user_with_email(email, password):
    user = auth.create_user_with_email_and_password(email, password)
    print(user)
    return user


def sign_in_user_with_email(email, password):
    user = auth.sign_in_with_email_and_password(email=email, password=password)
    print(user)
    return user


def signIn_user_with_token(token):
    user = auth.sign_in_with_custom_token(token)
    print(user)
    return user


def email_verifications(user):
    verification = auth.send_email_verification(user["idToken"])
    print(verification)
    return verification


def password_reset(email):
    password_rest = auth.send_password_reset_email(email)
    print(password_rest)
    return password_rest


def get_user_account_info(user):
    info = auth.get_account_info(user["idToken"])
    print(info)
    return info


if __name__ == "__main__":
    create_user_with_email("email here ", "password here ")
