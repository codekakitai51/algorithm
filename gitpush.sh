#!/bin/bash
git add .
git commit -m "$1"
git push origin main

# ex) ./gitpush.sh "This is a commit message"