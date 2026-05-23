# AsianSklad

Полноценный стартовый проект: **frontend (React)** + **backend (FastAPI)** для магазина грузовой техники, поставляемой из Китая в Россию.

## Структура
- `frontend/` — клиентская часть на React + Vite (4 страницы)
- `backend/` — API на FastAPI + SQLAlchemy
- `backend/sql/schema_and_queries.sql` — SQL-скрипт создания БД и проверочные запросы
- `docs/diploma_description.md` — текст для задания 1
- `docs/diagrams.md` — ER и Use-case диаграммы (Mermaid)

## Запуск frontend
```bash
cd frontend
npm install
npm run dev
```

## Запуск backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
