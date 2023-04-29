#!/bin/bash
# usage: sh ./upload_file.sh example_file.txt
# output: <File URL>
curl -s -F "file=@$1" -F "path=$2" -F "randomize_filename=$3" -F "keep_exif=$4" "http://0.0.0.0:9900/u"