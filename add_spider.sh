#!/usr/bin/bash

python add_service.py $1

if [ "$?" = 0 ]
then
	docker compose up --no-recreate -d --remove-orphans >/dev/null 2>&1
fi
