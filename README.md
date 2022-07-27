Тестовая задача - ТПАСС
Cервис-«укорачиватель ссылок»

telegram: @maxkorolyov

### Этапы запуска приложения на локальной машине:
1. Установите <a href=https://docs.docker.com/engine/install/ubuntu/>docker</a>
2. Клонируйте проект в рабочую директорию:<br> 
```https://github.com/pkrfc/shortURL.git```
3. Создайте файл .env (в директории /infra) с переменными окружения:<br> 
SECRET_KEY, DEBUG, ALLOWED_HOSTS, DB_ENGINE, DB_NAME, POSTGRES_USER, POSTGRES_PASSWORD, DB_HOST, DB_PORT<br>
4. Сборка и запуск контейнеров:<br>
```docker-compose up -d```<br>
5. Выполнить команды:<br>
```docker-compose exec infra-backend-1 python3 manage.py migrate```<br><br>
```docker-compose exec infra-backend-1 python3 manage.py collectstatic --no-input ```<br>