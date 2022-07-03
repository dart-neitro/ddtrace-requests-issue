ARG PYTHON_IMAGE=python
FROM ${PYTHON_IMAGE}:3.10-slim

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get install -y --fix-missing --no-install-recommends \
    build-essential \
    gcc \
    wget \
    libpq-dev \
    git

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.9.0/wait /wait
RUN chmod +x /wait

WORKDIR /app

RUN python -m pip install --upgrade pip

COPY requirements.txt requirements.txt

RUN python -m pip install -r requirements.txt --no-cache-dir

COPY . .

COPY ./run_app.sh /run_app.sh
RUN chmod +x /run_app.sh

CMD /wait && /run_app.sh