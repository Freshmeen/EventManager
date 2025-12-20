# Event Manager
Платформа для организации и сопровождения студенческих мероприятий. Проект призван систематизировать внеучебную деятельность, сохранить историю событий и справедливо оценить вклад каждого участника.

## Запуск приложения
1. Переходим в корневую папку проекта
2. Создаём виртуальное окружение
    ```bash
    python -m venv .venv
    ```
    и активируем его
    ```bash
    source .venv/bin/activate
    ```
3. Устанавливаем зависимости бэкенда
    ```bash
    pip install -r requirements/base.txt
    ```
4. Запускаем приложение
    ```bash
    uvicorn backend.app.main:app --reload
   ```

5. Открываем в браузере http://localhost:8000/openapi.json
   > Должна отобразиться разметка API приложения

Далее переходим к сборке [фронтенда](frontend/README.md)

После сборки фронтенда:
Перезапускаем приложение
```bash
uvicorn backend.app.main:app --reload
```
Открываем в браузере http://localhost:8000/. Должна отобразиться страница приложения

## База данных

### Миграции

1. Запуск базы данных

Поднимите контейнер с MySQL:
```bash
docker compose up --build -d
```
2. Применение миграций

Миграции запускаются локально из папки бэкенда.
Перейдите в папку `backend` и активируйте виртуальное окружение:
```bash
cd backend
source ../.venv/bin/activate
```
Выполните команду для создания таблиц (накат до последней версии):
```bash
alembic upgrade head
```

## Тестирование API

В проекте используются интеграционные тесты на стеке **pytest + pytest-asyncio + httpx**.
Тесты запускаются против реальной базы данных MySQL (создается отдельная БД `event_manager_test`), что гарантирует проверку работы всего пайплайна: от роутера до SQL-запросов.

### Запуск тестов

1. Убедитесь, что Docker-контейнер с MySQL запущен
```bash
docker compose up -d
```

2. Перейдите в папку бэкенда и активируйте окружение
```bash
cd backend
source ../.venv/bin/activate 
```

3. Запустите pytest
```bash 
pytest -v
```

### Написание новых тестов

Тесты располагаются в директории ./tests

Правила:
* Файл должен начинаться с test_.
* Функция теста должна быть асинхронной: async def test_....
* Класс с тестами должен быть помечен декоратором pytest.mark.asyncio (или настроен через pytest.ini).

Доступные фикстуры (в conftest.py):
* `client`: Асинхронный HTTP-клиент (httpx.AsyncClient), уже настроенный на работу с тестовой базой.
* `db_session`: Асинхронная сессия SQLAlchemy.
* `create_user_fixture`: Создает тестового пользователя и возвращает его данные (включая user_id).
* `create_event_fixture`: Создает тестовое событие и возвращает его данные.

Пример теста:
```python
import pytest
from httpx import AsyncClient

# Если используете класс, можно пометить весь класс
pytestmark = pytest.mark.asyncio

async def test_example_scenario(client: AsyncClient, create_user_fixture):
    # 1. Подготовка данных (через фикстуры или вручную)
    user_id = create_user_fixture["user_id"]
    
    # 2. Выполнение действия (запрос к API)
    response = await client.get(f"/api/v1/users/{user_id}")
    
    # 3. Проверка результата (Asserts)
    assert response.status_code == 200
    assert response.json()["email"] == "test@test.com"
```
