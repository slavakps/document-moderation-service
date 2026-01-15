# Document Moderation Service

Сервис модерации загружаемых документов.

Функционал:
- авторизованные пользователи загружают документы через API
- администратор получает email-уведомление о новой загрузке
- администратор в Django admin может подтвердить/отклонить документ
- пользователь получает email-уведомление о результате модерации
- отправка email выполняется через очередь (Celery + Redis)

Стек:
- Django, DRF
- PostgreSQL
- Celery + Redis
- Docker, Docker Compose
- Swagger (drf-spectacular)
- Pytest + coverage

## Структура проекта

- config/ — настройки проекта Django + celery app
- documents/ — приложение документов (модель, API, celery tasks, admin actions)
- docker-compose.yml — Postgres + Redis + backend + celery
- Dockerfile — сборка контейнера приложения
- .env.template — пример env переменных

## Переменные окружения

Создай файл `.env` в корне проекта (можно скопировать из `.env.template`).

Обязательные переменные:
- DJANGO_SECRET_KEY
- POSTGRES_DB
- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_HOST
- POSTGRES_PORT
- REDIS_URL
- EMAIL_BACKEND
- DEFAULT_FROM_EMAIL

## Запуск через Docker

1) Создать `.env`
2) Запустить:

```bash
docker-compose up --build
