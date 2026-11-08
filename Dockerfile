FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY apps ./apps
RUN pip install --no-cache-dir . && useradd --uid 10001 --create-home appuser
USER 10001
EXPOSE 8000
CMD ["uvicorn", "crip_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
