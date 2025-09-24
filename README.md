 # Backend Portfolio — Данил Мосейчук

Привет! Я начинающий backend-разработчик (Python). Ищу стажировку/джун позицию, предпочитаю удалёнку.

## Ключевые навыки
- Python (3.11+), Asyncio, typing
- HTTP-клиенты: httpx (async)
- REST / JSON, работа со сторонними API
- SQLAlchemy (async), PostgreSQL (базовый уровень)
- Очереди/события: RabbitMQ (базовый уровень), FastStream (запуск воркера)
- Git, GitHub/GitLab, MR/Code Review, .gitignore
- Docker (базово), uv (локальные окружения)

## Опыт
Стажёр Backend, AvtobusOnline  
- Реализовал адаптеры к кассовым провайдерам (**IQTech**, **eOFD**): приход, возврат, проверка статуса.  
- Группировка позиций (пассажирские/багажные), работа с НДС (VAT), сбор корректного JSON под API.  
- Поднимал локально сервис через uv, запускал воркер FastStream, тестировал обмены в RabbitMQ.  
- Наводил порядок в MR: .gitignore, удаление мусора, чистые ветки.  
- Сделал fallbacks: ретраи/проверка статуса/понятные ошибки.

## Проекты
- projects/iqtech_adapter — адаптер для провайдера IQTech (приход/возврат/статус, группировка позиций, VAT).
- projects/eofd_adapter — адаптер eOFD, сбор JSON без pydantic-моделей, VAT-map, возвраты по refund_amount.

> Код проектов и инструкции запуска — внутри соответствующих папок.

## Контакты
- Telegram: @notwhkuv
- Email: *(whokilleduverdosze4@gmail.com)

- [Demo Receipts](projects/demo-receipt) — формирование payload для чеков (income / income_return / status)

- [projects/fastapi-receipt](projects/fastapi-receipt) — мини-API на FastAPI: формирование JSON для приход/возврат/статус.

- [projects/fastapi-receipt](projects/fastapi-receipt) — мини-API на FastAPI: формирование JSON для приход/возврат/статус.
