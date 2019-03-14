#!/usr/bin/env bash
source /home/env/hibbienet/bin/activate
exec gunicorn -n hibbienet -w 3 -b 0.0.0.0:9000 hibbie.wsgi:application

