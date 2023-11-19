import pytest
import os
import boto3
from ..src import autoRsync




@pytest.fixture(scope="module")
def platform_test(source, dest):

    S3_TOKEN_ID='AWS_ACCESS_KEY_ID'
    S3_ACCESS_KEY='AWS_SECRET_ACCESS_KEY'
    

    ENV_VARS = (S3_TOKEN_ID, S3_ACCESS_KEY)
    NO_ENV_VARS = ' '.join(ENV_VARS)+' not in environment'

    s3 = boto3.resource(
        service_name = 's3',
        region_name='us-east-2',
        aws_access_key_id=S3_TOKEN_ID,
        aws_secret_access_key=S3_ACCESS_KEY
    )

    autoRsync.autoRsync.find_os(source=source, dest=dest)


#Connect to 2 S3 Instances, using $S3_TOKEN and $S3_TOKEN2 and perform tests with their respective OS's
#Transmit ~1 GB between the two and then back.
#

def test_test(platform_test):
    testpathA = 'testA/'
    testpathB = 'testB/'
    platform_test(testpathA, testpathB)
    assert(os.listdir(testpathA) == os.listdir(testpathB))