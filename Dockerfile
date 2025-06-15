FROM python:3.13-alpine

WORKDIR /app
RUN apk add --no-cache gcc musl-dev mariadb-connector-c-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["sh", "-c", "python3 -m alembic upgrade head && uvicorn app.main:app --host 0.0.0.0 --port 8000"]