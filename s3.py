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

	#
	# TODO:
	#
	# https://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Paginator.ListObjectVersions
	#
	# - get pagination working: look at MaxItems, NextToken, and StartingToken
	#
	# - function: get latest version of each item (look at date since we have deleted items (get number of versions and total size)
	# - funciton: get latest version of delete markers (look at date agani)
	# - function: combine both of those dicts into a dict that includes status, number of versions, and total size
	#
	for item in response_iterator:

		if "Versions" in item:		
			for row in item["Versions"]:
				row["LastModified"] = str(row["LastModified"])

		if "DeleteMarkers" in item:
			for row in item["DeleteMarkers"]:
				row["LastModified"] = str(row["LastModified"])

		if "Versions" in item:
			print("Versions")
			#print(json.dumps(item["Versions"], indent = 2))
			for row in item["Versions"]:
				print(row["Key"])

		if "DeleteMarkers" in item:
			print("Delete Markers")
			#print(json.dumps(item["DeleteMarkers"], indent = 2))
			for row in item["DeleteMarkers"]:
				print(row["Key"])



else:
	print("! ")
	print("! Please re-run this script with --bucket")
	print("! ")
	sys.exit(1)


# TODO
# Check old versions
# Check for deleted files
# Sum up space used



