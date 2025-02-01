FROM python:3.11-alpine
LABEL authors="amin"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

COPY ./scripts /scripts
COPY . /app/
COPY requirements.txt /app/

EXPOSE 8000

RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

RUN chmod -R +x /scripts


ENV PATH="/scripts:py/bin:$PATH"


CMD ["run.sh"]
