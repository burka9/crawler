#!/usr/bin/bash


# Function to install requirements
print() {
	echo "---------------------------------------"
	echo "$1"
	echo "---------------------------------------"
}

# Check if spider_name is "bbc" or "fanabc"
if [ "$spider_name" = "bbc" ] || [ "$spider_name" = "fanabc" ] || [ "$spider_name" = "reporter" ] || [ "$spider_name" = "wikipedia" ]; then
	# start crawl
	print "starting crawl for $spider_name"
	scrapy crawl "$spider_name"
else
	# generate spider
	touch /app/crawler/spiders/$spider_name.py
	print "generating spider: $spider_name with start_url: $start_url"
	python /app/gen_spider.py $spider_name $start_url


	# start crawl
	print "starting crawl for $spider_name"
	scrapy crawl "$spider_name"
fi

# end
print "crawl ended for $spider_name"

tree
cat /app/crawler/spiders/$spider_name.py | echo