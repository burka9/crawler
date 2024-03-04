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
		sudo docker compose up --build -d
	else
		sudo docker compose up --build
	fi
fi


echo "------------------------------"
echo "------------------------------"
echo "scrapy_crawler image build finished"
echo "------------------------------"
echo "------------------------------\n"