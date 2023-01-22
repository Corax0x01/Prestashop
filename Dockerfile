FROM alpine:3.5 as intermediate

RUN apk update
RUN apk add git

RUN git clone -b final https://github.com/Corax0x01/Prestashop.git

FROM prestashop/prestashop:1.7.8.7


COPY --from=intermediate /Prestashop/src .
RUN chmod -R 755 .
RUN chown -R www-data:www-data /var/www/html
RUN rm -rf install/

ARG DATABASE_HOST=be_184280_mariadb

RUN sed -i "s|'mariadb'|'${DATABASE_HOST}'|g" ./app/config/parameters.php

RUN mkdir docker
COPY --from=intermediate /Prestashop/docker/ssl/apache2/ /docker

EXPOSE 80
EXPOSE 443

RUN bash /docker/ssl.sh