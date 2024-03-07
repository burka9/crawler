#!/usr/bin/bash

echo "------------------------------"
echo "------------------------------"
echo "building scrapy_crawler image"
echo "------------------------------"
echo "------------------------------"


sudo docker build -t scrapy_crawler .

if [ "$1" = "run" ]
then
	if [ "$2" = "-d" ]
	then
		docker compose up --no-recreate -d --remove-orphans
	else
		docker compose up --no-recreate --remove-orphans
	fi
fi


echo "------------------------------"
echo "------------------------------"
echo "scrapy_crawler image build finished"
echo "------------------------------"
echo "------------------------------\n"