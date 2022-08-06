
FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/app"
ARG SSH_PRIVATE_KEY

COPY pyproject.toml poetry.lock ./

RUN mkdir /root/.ssh/ \
    && echo "${SSH_PRIVATE_KEY}" > /root/.ssh/id_rsa \
    && chmod -R 600 /root/.ssh/ \
    && ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -U poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root

WORKDIR /usr/src/app