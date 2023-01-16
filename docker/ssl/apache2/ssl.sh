#!/bin/bash

openssl req -newkey rsa:2048 -new -nodes -x509 -days 365 -keyout /etc/ssl/private/apache-selfsigned.key -out /etc/ssl/certs/apache-selfsigned.crt -subj "/C=PL/ST=Pomerania/L=Gdansk/O=PG/OU=./CN=."

rm -rf /etc/apache2/sites-available/000-default.conf

cp /docker/000-default.conf /etc/apache2/sites-available/000-default.conf

a2enmod ssl

echo "ServerName localhost" >> /etc/apache2/apache2.conf
service apache2 restart && sleep infinity