FROM ubuntu

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
	python-pip \
	python-setuptools \
    && rm -rf /var/lib/apt/lists/*

COPY ./ ./UrlShortener
WORKDIR ./UrlShortener
RUN pip install wheel
RUN pip install -r ./requirements.txt

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
