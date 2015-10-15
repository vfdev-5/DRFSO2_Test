#!/usr/bin/env bash

URL="http://127.0.0.1:8000/auth/register/"

# Existing user
username="userthree"
password="345"

curl -vvv -S -F "username=${userthree}" -F "password1=${password}" ${URL}
echo


