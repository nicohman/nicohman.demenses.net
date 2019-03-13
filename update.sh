#!/bin/bash
cd /var/www/nicohman
git reset --hard HEAD
git pull https://git.sr.ht/~nicohman/nicohman.demenses.net --force
python export.py &
