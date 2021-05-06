def lambda_handler(event, context):
    print("event " + str(event))
    print("context " + str(context))
    ec2_reg = boto3.client('ec2')
    regions = ec2_reg.describe_regions()
    for region in regions['Regions']:
        region_name = region['RegionName']
        instances = Ec2Instances(region_name)
        deleted_counts = instances.delete_snapshots(1)
        instances.delete_available_volumes()
        print("deleted_counts for region " +
              str(region_name) + " is " + str(deleted_counts))
        instances.shutdown()
        print("For RDS")
        rds = Rds(region_name)
        rds.cleanup_snapshot()
        rds.cleanup_instances()
    return 'Hello from Lambda'
