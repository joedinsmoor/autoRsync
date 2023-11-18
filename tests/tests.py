import pytest
import os
import boto3
from ..src import autoRsync


os.environ["AWS_DEFAULT_REGION"] = 'us-east-2'
os.environ["AWS_ACCESS_KEY_ID"] = $S3_TOKEN
os.environ["AWS_SECRET_ACCESS_KEY"] = $S3_KEY


@pytest.fixture(scope="module")
def platform_test():
    s3 = boto3.reosurce(
        service_name = 's3',
        region_name='us-east-2',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

    autoRsync.autoRsync.find_os('/testA/', '/testB/')


#Connect to 2 S3 Instances, using $S3_TOKEN and $S3_TOKEN2 and perform tests with their respective OS's
#Transmit ~1 GB between the two and then back.
#

def test_test(platform_test):
    testpathA = '/testA/'
    testpathB = '/testB/'
    platform_test()
    assert(os.listdir(testpathA) == os.listdir(testpathB))