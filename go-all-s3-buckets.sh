#!/bin/bash
#
# Wrapper for go.sh to run over all buckets
#

# Errors are fatal
set -e

# Change to the directory where this script is
pushd $(dirname $0) >/dev/null

for BUCKET in $(aws s3 ls |awk '{print $3}' )
do
	./go.sh $BUCKET
done 



