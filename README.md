
# S3 Disk Usage

Report S3 disk usage stats, including revisions and deleted files.

I wrote this tool in a fit of furstration when I was trying to determine when ~20 GB of 
files in my S3 buckets was being billed as 200 GB of storage.  You see, I really like having
versioning turned on for safety reasons, but disk space can shoot way up if there are many
versions of a file or if there are many deleted files.

This will report on total use across all versions of a file.


## Prerequisites

You will need to create an account in <a href="https://aws.amazon.com/iam/">AWS IAM</a> that
has read-only access to Amazon S3.  The permissions on that account should look something like this:

<img src="./img/aws-iam-policy.png" />

Then run `aws configure` from the command line, enter your credentials, and verify
that `aws s3 ls` works.


## Usage 

## Under The Hood










