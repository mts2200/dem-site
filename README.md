# Простое одностраничное веб приложение для теста студикам по развертыванию

Для запуска проекта необходимо создать .env файл или передавать вручную в докер. Пример заполненных env переменных лежит в файле .env.base

Если проект будет собираться через докер композ, то заменить

```
DB_HOST="host.docker.internal"
```

на

```
DB_HOST=service_name
```

Проект поддерживает два вида баз данных MariaDB и Postgres.
Чтобы указать с каким типом базы данных идет работа, заполнить переменную одним из значений
DB_TYPE=maria или DB_TYPE=postgres

Ниже следуют инструкции по сбору докер образов

Собрать образ с марией

```
docker build -t 'demo_site_maria' -f Dockerfile_maria .
```

Запустить марию

```
docker run --env-file .env -p 3306:3306 demo_site_maria
```

Собрать проект

```
docker build -t 'demo_site' -f Dockerfile .
```

Запустить проект

```
docker run --env-file .env -p 8030:8000 demo_site
```

Собрать образ с докером используя .env файл

```
docker build --build-arg DB_USER=$(grep DB_USER .env | cut -d '=' -f2) \
--build-arg DB_PASS=$(grep DB_PASS .env | cut -d '=' -f2) \
--build-arg DB_NAME=$(grep DB_NAME .env | cut -d '=' -f2) -t \
'demo_site_postgres' -f Dockerfile_postgres .
```

Запустить докер с постгрей

```
docker run --env-file .env -p 5436:5432 demo_site_postgres
```
