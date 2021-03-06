FROM python:3.7-slim-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
  # dependencies for building Python packages
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  && apt-get install -y libsm6 libxext6 libxrender-dev \
  && apt install -y python-tk ghostscript \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

#RUN addgroup --system django \
#    && adduser --system --ingroup django django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/test.txt \
    && rm -rf /requirements

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint
#RUN chown django /entrypoint

COPY ./compose/test/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start
#RUN chown django /start
COPY ./compose/test/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r$//g' /start-celeryworker
RUN chmod +x /start-celeryworker
#RUN chown django /start-celeryworker

COPY ./compose/test/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r$//g' /start-celerybeat
RUN chmod +x /start-celerybeat
#RUN chown django /start-celerybeat

COPY ./compose/test/django/celery/flower/start /start-flower
RUN sed -i 's/\r$//g' /start-flower
RUN chmod +x /start-flower
COPY . /app
#COPY --chown=django:django . /app

COPY ./compose/test/django/services.json /services.json

#USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
