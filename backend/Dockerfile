FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

WORKDIR /app/

# Allow installing dev dependencies to run tests
# ARG INSTALL_DEV=false

COPY ./requirements.txt /app/

RUN bash -c "pip install -r ./requirements.txt"

ENV PYTHONPATH=/app

COPY ./app /app/app