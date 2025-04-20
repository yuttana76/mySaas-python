### Create project call visits
``` bash
django-admin startapp visits
```

### Add in setting.py file
```
INSTALLED_APPS = [
    #Django Apps
   ...
    # Custom My Apps
    "visits",
]
```

### Make Migrations
```
python manage.py makemigrations
python manage.py migrate

```

### run server
```
python manage.py runserver
```