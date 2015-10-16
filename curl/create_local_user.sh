#!/usr/bin/env bash

URL="http://127.0.0.1:8000/api/register/"

username="userone"
password="123"
email="u1@email.com"

curl -X POST -d "username=${username}&password=${password}&email=${email}" ${URL}
echo


