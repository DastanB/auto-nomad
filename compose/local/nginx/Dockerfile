FROM python:3.7-slim-buster as build-stage

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update \
    # dependencies for building Python packages
    && apt-get install -y build-essential \
    # psycopg2 dependencies
    && apt-get install -y libpq-dev \
    # Translations dependencies
    && apt-get install -y gettext \
    # Uncomment below lines to enable Sphinx output to latex and pdf
    # && apt-get install -y texlive-latex-recommended \
    # && apt-get install -y texlive-fonts-recommended \
    # && apt-get install -y texlive-latex-extra \
    # && apt-get install -y latexmk \
    # cleaning up unused files
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
# All imports needed for autodoc.
RUN pip install -r /requirements/local.txt

COPY ./docs /docs
COPY ./config /config
COPY ./nomad_auto_advert /app/nomad_auto_advert

WORKDIR /docs

CMD make build


FROM nginx:1.19

COPY --from=build-stage /docs/_build/dist/ /usr/share/nginx/html

COPY compose/local/nginx/site.nginx.conf /etc/nginx/conf.d/default.conf
COPY compose/local/nginx/nginx.conf /etc/nginx/nginx.conf
