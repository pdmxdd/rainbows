#!/bin/bash

curl -XPOST 127.0.0.1:8888/register -H 'Content-Type: application/json' -d '
{
    "email": "pdmxdd@gmail.com",
    "password": "password"
}'