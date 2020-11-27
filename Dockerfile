FROM python:3.7.8
ENV PYTHONUNBUFFERED=1 \
    POETRY_VERSION=1.1.4

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

WORKDIR /app

COPY poetry.lock pyproject.toml /app/
RUN pip3 install --no-cache-dir --upgrade pip uwsgi && \
    poetry config virtualenvs.create false && poetry install && \
    rm -rf /root/.cache/

COPY ./ /app/main/

WORKDIR /app/main/

RUN python ./manage.py migrate --no-input
RUN python ./manage.py collectstatic --no-input

EXPOSE 9000
ENTRYPOINT []
CMD ["uwsgi", "/app/main/uwsgi.ini"]