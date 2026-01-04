#!/bin/bash
set -e

echo "==> Waiting for PostgreSQL..."
TIMEOUT=30
ELAPSED=0
RETRY_INTERVAL=2

# Attempt to connect to PostgreSQL database.
until PGPASSWORD="$DB_PASSWORD" psql -h "$DB_HOST" -U "$DB_USER" -d "$DB_NAME" -c '\q' 2>/dev/null; do
  if [ $ELAPSED -ge $TIMEOUT ]; then
    echo "    ERROR: PostgreSQL not available after ${TIMEOUT}s"
    exit 1
  fi
  echo "    PostgreSQL is unavailable - sleeping (${ELAPSED}/${TIMEOUT}s)"
  sleep $RETRY_INTERVAL
  ELAPSED=$((ELAPSED + RETRY_INTERVAL))
done
echo "    PostgreSQL is ready - continuing"

# Run database migrations.
echo "==> Running database migrations..."
if ! alembic upgrade head; then
  echo "    ERROR: Migration failed"
  exit 1
fi
echo "    Migrations complete"

echo "==> Starting Discord bot..."
exec "$@"
