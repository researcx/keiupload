#!/bin/bash
uwsgi --socket 0.0.0.0:9900 --wsgi-file keiupload.py --master --enable-threads --workers 4 --processes 4 --threads 4 --callab app