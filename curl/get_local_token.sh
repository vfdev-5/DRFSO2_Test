#!/usr/bin/env bash


URL="http://127.0.0.1:8000/auth/token/"

client_id="KSo05DIhGLGiKcJuraW0hvORl68WyfhBUhrjkZoE"
client_secret="C5tdn1Q0NW95sd8MmJFm64SObyjGUv1pnXmCHebJ1hSkWHKXQqR3OhJTLHPAoMJVaKpfRM59iy29z7WpIQsZyGrH670FgZ9R5FeHzKU4tyuAvmq9t5IpNn6zGEZlwSzW"

# Existing user
username="userthree"
password="345"

curl -vvv -X POST -d "client_id=${client_id}&client_secret=${client_secret}&grant_type=password&username=${username}&password=${password}" ${URL}
echo



## From https://github.com/evonove/django-oauth-toolkit/issues/147
#curl -v -X POST -u "${userthree}:${password}" -d "grant_type=client_credentials" ${URL}
