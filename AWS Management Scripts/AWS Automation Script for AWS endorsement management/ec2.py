from datetime import datetime, timedelta, timezone

import boto3


def get_delete_data(older_days):
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=older_days)
    return delete_time


def is_ignore_shutdown(tags):
    for tag in tags:
        print("K " + str(tag['Key']) + " is " + str(tag['Value']))
        if str(tag['Key']) == 'excludepower' and str(tag['Value']) == 'true':
            print("Not stopping K " +
                  str(tag['Key']) + " is " + str(tag['Value']))
            return True
    return False


def is_unassigned(tags):
    if 'user' not in [t['Key'] for t in tags]:
        return True
    return False


class Ec2Instances(object):

    def __init__(self, region):
        print("region " + region)

        # if you are not using AWS Tool Kit tool you will be needing to pass your access key and secret key here

        # client = boto3.client('rds', region_name=region_name, aws_access_key_id=aws_access_key_id,
        #                       aws_secret_access_key=aws_secret_access_key)
        self.ec2 = boto3.client('ec2', region_name=region)

    def delete_snapshots(self, older_days=2):
        delete_snapshots_num = 0
        snapshots = self.get_nimesa_created_snapshots()
        for snapshot in snapshots['Snapshots']:
            fmt_start_time = snapshot['StartTime']
            if fmt_start_time < get_delete_data(older_days):
                try:
                    self.delete_snapshot(snapshot['SnapshotId'])
                    delete_snapshots_num + 1
                except Exception as e:
                    print(e)
        return delete_snapshots_num

    def get_user_created_snapshots(self):
        snapshots = self.ec2.describe_snapshots(
            Filters=[{
                'Name': 'owner-id', 'Values': ['your owner id'],
            }])  # Filters=[{'Name': 'description', 'Values': ['Created by Nimesa']}]
        return snapshots

    def delete_available_volumes(self):
        volumes = self.ec2.describe_volumes()['Volumes']
        for volume in volumes:
            if volume['State'] == "available":
                self.ec2.delete_volume(VolumeId=volume['VolumeId'])

    def delete_snapshot(self, snapshot_id):
        self.ec2.delete_snapshot(SnapshotId=snapshot_id)

    def shutdown(self):
        instances = self.ec2.describe_instances()
        instance_to_stop = []
        instance_to_terminate = []
        for res in instances['Reservations']:
            for instance in res['Instances']:
                tags = instance.get('Tags')
                if tags is None:
                    instance_to_terminate.append(instance['InstanceId'])
                    continue
                if is_unassigned(tags):
                    print("instance_to_terminate " + instance['InstanceId'])
                    instance_to_terminate.append(instance['InstanceId'])
                if is_ignore_shutdown(tags):
                    continue
                if instance['State']['Code'] == 16:
                    instance_to_stop.append(instance['InstanceId'])

        if any(instance_to_stop):
            self.ec2.stop_instances(
                InstanceIds=instance_to_stop
            )
        if any(instance_to_terminate):
            print(instance_to_terminate)
            self.ec2.terminate_instances(
                InstanceIds=instance_to_terminate
            )


if __name__ == "__main__":
    ec2 = Ec2Instances('us-east-1')
    ec2.delete_snapshots(3)
    ec2.shutdown()
