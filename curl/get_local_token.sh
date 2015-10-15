#!/usr/bin/env bash


URL="http://127.0.0.1:8000/auth/token/"

client_id="X77NW6JwLvdWJk4q49ycM7QgDGgNujcnvP4Jn8ik"
client_secret="4bJEKqU10Sp7skwgoDfK6TzvljsiV1pOGgulSdnO6OdRiSAxQh7AFAsb9RRDlxEMWfYHhwvXiYXUIfNIUbRy5GiLXaKblXTzsicdLZepdg3ZMYEjMQLwI5BKF2sZuPTU"

# Existing user
username="userone"
password="123"

curl -vvv -X POST -d "client_id=${client_id}&client_secret=${client_secret}&grant_type=password&username=${username}&password=${password}" ${URL}
echo

