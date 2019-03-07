#!/bin/bash
git reset --hard HEAD
git pull https://git.sr.ht/~nicohman/nicohman.demenses.net --force
python app.py &
