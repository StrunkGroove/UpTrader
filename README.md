# UpTrader

### For download and start:
```
git clone https://github.com/StrunkGroove/UpTrader.git && \
cd ./UpTrader && \
docker-compose --env-file .env.dev up
```

### For applying migrations
#### Enter in docker
```
docker-compose exec -it web bash
```
#### Applying migrations
```
python manage.py makemigrations && python manage.py migrate
```
#### Fill DB
```
python data_for_fill_db.py
```
#### Create superuser
```
python manage.py createsuperuser --username admin@mail.ru --email admin@mail.ru
```
### For applying migrations and fill db and create user:
```
