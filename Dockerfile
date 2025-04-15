FROM python:3.13

RUN pip install --no-cache-dir uv

ARG workdir=/fastapi-telegram-bot
ARG PORT=7777

ENV WORKDIR=${workdir}
ENV PORT=${PORT}

WORKDIR ${WORKDIR}

COPY pyproject.toml uv.lock ${WORKDIR}/
COPY .env.example ${WORKDIR}/.env

RUN uv venv && uv sync

COPY . ${WORKDIR}/

SHELL ["/bin/bash", "-c"]
ENV PATH="${WORKDIR}/.venv/bin:$PATH"

CMD uvicorn src.app:app --host 0.0.0.0 --port ${PORT}