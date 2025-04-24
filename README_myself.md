
Python Tutorial: Build a SaaS App with Django, Stripe, Neon PostgreSQL, TailwindCSS, GitHub Actions
youtube
https://www.youtube.com/watch?v=WbNNESIxJnY&t=371s

Code
https://github.com/codingforentrepreneurs/SaaS-Foundations/blob/main/src/cfehome/settings.py

User name
devone
passdev


yuttana76
Mpam@2025

### Should try
django-storages

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

### Sending Emails with Gmail
```
python manage.py sendtestemail --admin
```

### Creat supersuer / admin user
```
python manage.py createsuperuser
```

Advance tool
```
python manage.py shell
```

### Create Auth app for login & registration
```
python manage.py startapp auth
```

### allauth.org
https://docs.allauth.org/en/latest/installation/quickstart.html
Do config and run migrate 
```
python manage.py migrate
```
test
http://localhost:8000/accounts/login/

### allauth config is important
https://docs.allauth.org/en/latest/account/configuration.html

### New for allauth-ui reference
https://github.com/danihodovic/django-allauth-ui

### Customize allauth-ui reference this link
https://github.com/danihodovic/django-allauth-ui?tab=readme-ov-file#hacking-on-the-project

### User profle
Run command
```
python manage.py startapp profiles
```

Config in setting.py
```
INSTALLED_APPS=[
    ...
    "profiles",
    ...
]
```
