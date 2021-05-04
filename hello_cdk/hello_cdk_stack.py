from aws_cdk import core as cdk

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.
from aws_cdk import core

from aws_cdk import aws_s3 as s3

class HelloCdkStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(self, 
            id='MyFirstBucket',
            bucket_name='mjheitland-my-first-bucket',
            versioned=False,
            removal_policy=core.RemovalPolicy.DESTROY, # what happens to the resource (i.e. bucket) if the CFN stack gets deleted: default = DESTORY, alternative: RETAIN and SNAPSHOT
            auto_delete_objects=True,
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            access_control=s3.BucketAccessControl.PRIVATE,
            # todo disable object deletion for prod, not yet supported in CDK
        )
