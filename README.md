# UpTrader

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
 
