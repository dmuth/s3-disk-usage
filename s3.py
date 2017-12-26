#!/usr/bin/env python3
#
# This script is used for exploring AWS S3 buckets, 
# getting old versions of files, and (optionally) deleting
# those old versions.
#

import argparse
import json
import logging
import sys

import boto3


logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger()

#
# Parse our arguments.
#
parser = argparse.ArgumentParser(description = "Explore versioned files in S3 buckets")
parser.add_argument("--bucket", help = "Bucket to operate on")
parser.add_argument("--filter", help = "Filename text to filter on")

args = parser.parse_args()
logger.info("Args: %s" % args)


s3 = boto3.resource("s3")

if not args.bucket:

	print("# ")
	print("# Our list of buckets.")
	print("# Please re-run this script with --bucket to choose a bucket")
	print("# ")

	for bucket in s3.buckets.all():
		print(bucket.name)

elif args.bucket:
	name = args.bucket
	logger.info("Exploring bucket '%s'..." % name)

	client = boto3.client("s3")
	paginator = client.get_paginator("list_object_versions")

	response_iterator = paginator.paginate(
		Bucket = name,
		Prefix = ""
		)

	for item in response_iterator:

		if "Versions" in item:		
			for row in item["Versions"]:
				row["LastModified"] = str(row["LastModified"])

		if "DeleteMarkers" in item:
			for row in item["DeleteMarkers"]:
				row["LastModified"] = str(row["LastModified"])

		if "Versions" in item:
			print("Versions")
			print(json.dumps(item["Versions"], indent = 2))

		if "DeleteMarkers" in item:
			print("Delete Markers")
			print(json.dumps(item["DeleteMarkers"], indent = 2))
	




else:
	print("! ")
	print("! Please re-run this script with --bucket")
	print("! ")
	sys.exit(1)


# TODO
# Check old versions
# Check for deleted files
# Sum up space used



