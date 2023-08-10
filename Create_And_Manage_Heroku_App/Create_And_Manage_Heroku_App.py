import heroku3

def create_heroku_app(app_name):
    heroku_conn = heroku3.from_key('YOUR_HEROKU_API_KEY')  # Replace with your Heroku API key or use heroku3.from_key(heroku_api_key)
    app = heroku_conn.create_app(name=app_name)
    return app

def list_heroku_apps():
    heroku_conn = heroku3.from_key('YOUR_HEROKU_API_KEY')  # Replace with your Heroku API key or use heroku3.from_key(heroku_api_key)
    apps = heroku_conn.apps()
    return apps

def delete_heroku_app(app_name):
    heroku_conn = heroku3.from_key('YOUR_HEROKU_API_KEY')  # Replace with your Heroku API key or use heroku3.from_key(heroku_api_key)
    app = heroku_conn.apps().get(app_name)
    if app:
        app.delete()
        print(f"App '{app_name}' deleted successfully.")
    else:
        print(f"App '{app_name}' not found.")

def main():
    app_name = input("Enter the name of the Heroku app: ")

    # Create a new Heroku app
    new_app = create_heroku_app(app_name)
    print(f"Heroku app '{new_app.name}' created successfully.")

    # List all Heroku apps
    print("\nList of all Heroku apps:")
    apps = list_heroku_apps()
    for app in apps:
        print(app.name)

    # Delete a Heroku app
    delete_app = input("Enter the name of the app to delete: ")
    delete_heroku_app(delete_app)

if __name__ == "__main__":
    main()s