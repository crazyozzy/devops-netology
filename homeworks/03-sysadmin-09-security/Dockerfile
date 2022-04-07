FROM httpd:2.4
COPY ./kda_sample/ /usr/local/apache2/htdocs
COPY ./my-httpd.conf /usr/local/apache2/conf/httpd.conf
COPY ./server.crt /usr/local/apache2/conf/server.crt
COPY ./server.key /usr/local/apache2/conf/server.key