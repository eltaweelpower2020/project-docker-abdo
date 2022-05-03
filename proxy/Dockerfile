FROM nginx:latest
EXPOSE  80
COPY ./default.conf /etc/nginx/conf.d/default.conf
COPY ./uwsgi_params /etc/nginx/uwsgi_params
USER root
RUN mkdir -p /vol/static
RUN chmod 755 /vol/static
RUN chmod 755 /etc/nginx/conf.d/default.conf
RUN chmod 755 /etc/nginx/uwsgi_params
CMD ["nginx", "-g", "daemon off;"]