#!/bin/bash
git add .
git commit -m "$1"
git push origin main

# use the script
# ./gitpush.sh "This is a commit message"