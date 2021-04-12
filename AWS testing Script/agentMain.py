from flask import Flask
from flask_ngrok import run_with_ngrok
import awstesting.awsTester as aws_testing

app = Flask(__name__)

# run_with_ngrok(app)


@app.route("/", methods=['POST', 'GET'])
def welcome():
    message = "Welcome to create your own test Api for AWS for Ec2 just use your Url/ec2 and your 100 ec2 " \
              "instance will be created in test environment if you dont want to use it in api based " \
              "just go to code and use awsTesting class and done "
    return message


# this api is to create an ec2 for testing

@app.route("/ec2", methods=['POST', 'GET'])
def ec2():
    client = aws_testing.add_service("ec2", "us-east-1")
    return aws_testing.test_create_ec2(client)


# you can add more apis of your choice here like
# create Volume, VPC and snapshots

# to do so just add a call function in awsTester class and agentMain and you are done

# run the app
if __name__ == '__main__':
    app.run()
