import boto3
s3 = boto3.resource('s3')
print('s3 buckets with name')
for bucket in s3.buckets.all():
    print(bucket)
ec2 = boto3.resource('ec2')
print('EC2 Instances in us-east-1 region')

for inst in ec2.instances.all():
    print(inst.id , inst.state['Name'])
region = input('Enter AWS Region: ')
ec2_1 = boto3.resource('ec2',region_name = region)
print(f'EC2 Instances in {region}')
for inst in ec2_1.instances.all():
    print(inst.id , inst.state['Name'])