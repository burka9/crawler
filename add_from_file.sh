#!/usr/bin/bash

python add_from_file.py $1

if [ "$?" = 0 ]
then
	docker compose up --no-recreate -d --remove-orphans &
fi