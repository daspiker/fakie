#!/bin/bash
source venv/bin/activate
flask db upgrade
service cron start
exec sudo -u fakie gunicorn -b :5000 --access-logfile - --error-logfile - fakie:app


