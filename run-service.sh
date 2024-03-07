#!/usr/bin/bash

chmod +x up.sh

sudo cp -f crawler.service /etc/systemd/system

sudo systemctl enable crawler.service
sudo systemctl restart crawler.service
