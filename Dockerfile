FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PATH="/scripts:${PATH}"
COPY  ./requirements.txt /requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade pip \
&& python3 -m pip install --no-cache-dir -r /requirements.txt \
&& python3 -m pip install --no-cache-dir PyYAML 
RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./scripts /scripts
RUN chmod +x /scripts/*
RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN chmod -R 755 /vol/web
CMD ["entrypoint.sh"]