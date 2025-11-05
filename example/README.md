# Example
Это пример приложения, на который можно опираться, когда пытаетесь в чём-то разобраться

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
    uvicorn example.backend.app.main:app --reload
   ```

5. Открываем в браузере http://localhost:8000/openapi.json
   > Должна отобразиться разметка API приложения

Далее переходим к сборке [фронтенда](frontend/README.md)

После сборки фронтенда:
Перезапускаем приложение
```bash
uvicorn example.backend.app.main:app --reload
```
Открываем в браузере http://localhost:8000/. Должна отобразиться страница приложения