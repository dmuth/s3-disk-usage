#!/usr/bin/env python3
#
# This script is used to extract the contents of an S3 bucket, including
# verison info and files that have been deleted.
#
# Note that we're using subprocess, as it appears to be a replacement
# for os.system() and other functions, as per https://stackoverflow.com/a/4813571/196073
#



import argparse
import json
import logging
import os
import subprocess
import sys
import tempfile


logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(levelname)s: %(message)s')
logger = logging.getLogger()

#
# Parse our arguments.
#
parser = argparse.ArgumentParser(description = "Extract all versions of files in an S3 bucket")
parser.add_argument("bucket")
#parser.add_argument("--filter", help = "Filename text to filter on")

args = parser.parse_args()
logger.info("Args: %s" % args)

output = "output.json"

bucket = args.bucket
cmd = "aws s3api list-object-versions --bucket %s" % bucket
#cmd = "ls what" # Debugging

tmp_fd, tmpfile = tempfile.mkstemp(dir=".", prefix="tmp-output")
logger.info("Temp file '%s' created!", tmpfile)

logger.info("Executing command '%s'" % cmd)
logger.info("Note that this may take a long time, perhaps a minute or more!")
completed = subprocess.run(cmd, stdout=tmp_fd, shell = True)


if completed.returncode:
	logger.error("! Process '%s' exited with return code '%d'" % (cmd, completed.returncode))
	sys.exit(completed.returncode)

logger.info("Renaming temp file '%s' to '%s'..." % (tmpfile, output))
os.rename(tmpfile, output)




