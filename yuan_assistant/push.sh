#! /usr/bin/bash
PROGDIR=$(dirname $(readlink -f "$0"))
cd $PROGDIR
git add ./
git commit
git push