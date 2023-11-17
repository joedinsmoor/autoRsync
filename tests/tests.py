import pytest
import os
from .src import autoRsync


@pytest.fixture(scope="module")
def platform_test():
    autoRsync.find_os('/testA/', '/testB/')

#Connect to 2 S3 Instances, using $S3_TOKEN and $S3_TOKEN2 and perform tests with their respective OS's
#Transmit ~1 GB between the two and then back.
#

def test_test(platform_test):
    testpathA = '/testA'
    testpathB = '/testB'
    platform_test()
    assert(os.listdir(testpathA) == os.listdir(testpathB))