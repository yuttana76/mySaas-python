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

### set local environment
```
export DJANGO_DEBUG="False"
```

### Secret Key for Django [blog pos
https://www.codingforentrepreneurs.com/blog/create-a-one-off-django-secret-key

```
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

OR
```
openssl rand -base64 32
```

### Config db
after config db run command
```
cd src

python manage.py migrate
```

### flowbite CDN
https://flowbite.com/docs/getting-started/quickstart/#include-using-cdn



### static files
Config in setting 

Don't save static files in git
.gitignor

```
python manage.py collectstatic 

```

### Custom python manange.py
```
python manage.py startapp commando
```
Create custom function in
commando/commands/hello_world.py

Run custom function 
```
python manage.py hello_world
```

For download static files
```
python manage.py vendor_pull
python manage.py collectstatic
```