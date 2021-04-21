import boto3
import boto.sqs
from boto.s3.key import Key
from moto import mock_ec2, mock_s3
import awstesting.awsHandler as aws


def add_service(service_name, region):
    aws_client = boto3.client(service_name, region_name=region)
    return aws_client


@mock_ec2
def test_create_ec2(aws_client):
    # demo ami
    ami_id = "ami-123"
    count = 100
    aws.create_ec2(aws_client, ami_id, count)
    instances = aws_client.describe_instances()['Reservations'][0]['Instances']
    for i in instances:
        print(i)
    if len(instances) == count:
        return "ec2 created successfully Insatnce ID = " + instances[0]['InstanceId'] + ""
    else:
        return "ec2 not created "


@mock_s3
def test_s3():
    print('Testing moto S3')

    # create bucket
    bucket_name = 'bucket1'
    conn = boto.connect_s3()
    print('Creating bucket: {}'.format(bucket_name))
    bucket = conn.create_bucket(bucket_name)

    # add object
    k = Key(bucket)
    key_name = 'file1'
    k.key = key_name
    k.set_contents_from_string('hello world')

    # list objects
    print('List of files:')
    for key in bucket.list():
        print('    {}/{}'.format(key.bucket.name, key.name))

    # get object
    k2 = Key(bucket)
    k2.key = key_name
    data = k2.get_contents_as_string()
    print('Fetched object {}/{} with content: {}'.format(bucket.name,
                                                         key.name, data))


if __name__ == "__main__":
    client = add_service("ec2", "us-east-1")
    test_create_ec2(client)
