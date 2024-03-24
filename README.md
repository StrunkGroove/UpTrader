# UpTrader

### Task
---
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.

### For download and start docker-compose:
```
git clone https://github.com/StrunkGroove/UpTrader.git && \
cd ./UpTrader && \
docker-compose --env-file .env.dev up -d 
```

### For setup app
#### Enter Docker container:
```
docker-compose --env-file .env.dev exec -it web bash
```
#### Applying migrations
```
python manage.py makemigrations && python manage.py migrate
```
#### Fill database
```
python data_for_fill_db.py
```
#### Create superuser
```
python manage.py createsuperuser --username admin@mail.ru --email admin@mail.ru
```

### Django available:
Url: http://localhost:8000  
Name superuser: admin@mail.ru  
Password: "your password in this step 'Create superuser' "
 
