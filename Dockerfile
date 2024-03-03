# generate docker file for scrapy
FROM python:3.10.8

# Install tree from apt
RUN apt-get update && apt-get install -y tree

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# cd to crawler directory
WORKDIR /app/crawler

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY entry.sh /app/entry.sh
RUN chmod +x /app/entry.sh

CMD ["bash", "/app/entry.sh"]
