FROM python:3.10.10-bullseye

ENV PATH /root/.local/bin:$PATH

WORKDIR /app

COPY ["./app/pyproject.toml", "./app/poetry.lock", "/app/"]

RUN apt-get update \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.create false \
    && poetry install

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]