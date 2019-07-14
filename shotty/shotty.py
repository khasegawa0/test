import boto3
import sys

session = boto3.Session(profile_name='shotty')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "list EC2 instances"
    for i in ec2.instances.all():
        print(',''.join((
        i.# IDEA: i.instance_type,
        i.placement['availablityzone'],
        i.state['name'],
        i.public_dns_name)))

    return

if __name__ == '__main__':
    list_instances()
