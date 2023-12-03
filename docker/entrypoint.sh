#!/bin/bash

set -eo pipefail

DAY="${1}"

cd /code/day${DAY}/

if [ -f "part2.py" ] ; then
    time sh -c 'python ./part1.py; python ./part2.py'
elif [ -f "puzzle.py" ] ; then
    time sh -c 'python ./puzzle.py'
else
    echo "not sure how to run this"
    exit 1
fi
