
# S3 Disk Usage

Report S3 disk usage stats, including revisions and deleted files.

I wrote this tool in a fit of furstration when I was trying to determine when ~20 GB of 
files in my S3 buckets was being billed as over 200 GB of storage.  You see, I really like having
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

### Quick and Dirty Version

Run `./go.sh bucketname`.

That will download a listing of all versions and all deleted files in a bucket and print out 
a nice human-readable display that looks something like this:

<img src="./img/s3-bucket-usage.png" />

As you can see, usage the bucket is reasonable, but there were over 200 GB of deleted
files present.  (As it turned out, there was a bucket policy that retained old/deleted versions 
for 365 days--oops!)

### More Detailed Usage

There are two core Python scripts: one to download the bucket contents, and one to
go through the resulting JSON and print up stats.  The syntax for each of these is:

`./1-get-bucket-contents.py bucket [file]`

The optional file is the name of the file to write the JSON data to.  The default
location is `output.json`.

The syntax for the second script is:

`./2-process-bucket-contents.py [--humanize] [file]`

If no file is specified, `output.json` will be read from.  Normally, the output
is in JSON format, but if you specify `--humanize` (as the `go.sh` script does), you
will get lovely human-readable output.


## Under The Hood













