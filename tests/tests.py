import pytest
import os
import boto3
from ..src.autoRsync import autoRsync




@pytest.fixture()
def platform_test():

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

    autoRsync.find_os(source='testA/', dest='testB/') # type: ignore


#Connect to remote S3 container, transmit file from one folder to another, then transmit locally and back
def test_test(platform_test):
    testpathA = 'testA/'
    testpathB = 'testB/'
    if not (os.path.isdir(testpathB)):
        os.mkdir(testpathB)
    autoRsync.find_os(source='testA/', dest='testB/') # type: ignore
    assert(os.listdir(testpathA) == os.listdir(testpathB))