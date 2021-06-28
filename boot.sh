#!/bin/bash
source venv/bin/activate
flask db upgrade
/usr/sbin/crond -f -l 8
exec gunicorn -b :5000 --access-logfile - --error-logfile - fakie:app


