#!/bin/bash 

DATABASE_NAME="prestashop" 
DATABASE_ROOT_PASSWORD="root" 
DATABASE_ROOT_LOGIN="root" 
DUMP_FILE="./db/backup.sql" 

docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysqldump -u$DATABASE_ROOT_LOGIN -p$DATABASE_ROOT_PASSWORD $DATABASE_NAME > $DUMP_FILE