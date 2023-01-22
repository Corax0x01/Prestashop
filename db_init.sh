#!/bin/bash

DATABASE_NAME="prestashop"
DATABASE_USER="be_184280"
DATABASE_PASSWORD="password"
DB_DUMP="./db/backup.sql"

docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysql -uroot -proot -e "CREATE DATABASE IF NOT EXISTS ${DATABASE_NAME};"
docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysql -uroot -proot -e "CREATE USER IF NOT EXISTS ${DATABASE_USER}@'%' IDENTIFIED BY '${DATABASE_PASSWORD}';"
docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysql -uroot -proot -e "GRANT ALL PRIVILEGES ON ${DATABASE_NAME}.* TO '${DATABASE_USER}'@'%';"
docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysql -uroot -proot -e "FLUSH PRIVILEGES;"
docker exec BlyskawicaPottera_be_184280_mariadb.1.m9diasj2fqbck1x7t0iihhnn2 mysql -uroot -proot $DATABASE_NAME < $DB_DUMP