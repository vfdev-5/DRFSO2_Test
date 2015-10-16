#!/usr/bin/env bash

URL="http://127.0.0.1:8000/api/protected/"

# Local user
token="B7P5OonauqmFskushntreYDZcR8Tw5"
curl -v -H "Authorization: Bearer ${token}" ${URL}

# Social network user
#backend="github"
#token="0fefa0f44ec3d2941dbdbc3870fb5d1cab3f5483"
#curl -v -H "Authorization: Bearer ${backend} ${token}" ${URL}