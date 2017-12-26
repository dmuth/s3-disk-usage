#!/usr/bin/env python3
#
# This script is used for exploring AWS S3 buckets, 
# getting old versions of files, and (optionally) deleting
# those old versions.
#

import argparse
import logging
import sys

import boto3


logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger()

#
# Parse our arguments.
#
parser = argparse.ArgumentParser(description = "Explore versioned files in S3 buckets")
parser.add_argument("--list-buckets", action = "store_true", help = "List buckets and exit")
parser.add_argument("--bucket", help = "Bucket to operate on")
parser.add_argument("--filter", help = "Filename text to filter on")

args = parser.parse_args()
logger.info("Args: %s" % args)


s3 = boto3.resource("s3")

if args.list_buckets:

	print("# ")
	print("# Our list of buckets.")
	print("# Please re-run this script with --bucket to choose a bucket")
	print("# ")

	for bucket in s3.buckets.all():
		print(bucket.name)

else:
	print("! ")
	print("! Please re-run this script with --list-buckets or --bucket")
	print("! ")
	sys.exit(1)


# TODO
# Get versions
# Check old versions
# Check for deleted files
# Sum up space used



