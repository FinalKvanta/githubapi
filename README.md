# Тестирование работы с GitHub API

## Описание
Проект демонстрирует взаимодействие с GitHub API. Скрипт может создавать, проверять и удалять публичный репозиторий на GitHub.

## Установка и запуск

1. **Клонируйте репозиторий**

    ```bash
    git clone https://github.com/FinalKvanta/githubapi.git
    cd githubapi
    ```

2. **Установите зависимости**

    ```bash
    # Для macOS
    python3 -m pip install -r requirements.txt

    # Для Windows
    python -m pip install -r requirements.txt
    ```

3. **Настройте файл .env**

    Создайте файл `.env` в корне проекта и добавьте в него ваши переменные:

    ```bash
    GIT_TOKEN=ваш_токен
    GIT_USER=ваш_юзернейм
    REPOS_PATH=путь_к_репозиторию
    ```

4. **Запустите файл**

    ```bash
    # Для macOS
    python3 test_api.py

    # Для Windows
    python test_api.py
    ```