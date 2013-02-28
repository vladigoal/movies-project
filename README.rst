===============================================
Movies project
===============================================


Deploy
======

2. Clone repository to server.
3. cd to cloned repository.
4. Setup virtual environment::

     virtualenv --no-site-packages -p python2.6 .env
     source .env/bin/activate

5. Run next commands in the commandline::

     PROJ_NAME=movies
     cp Makefile.def.default Makefile.def
     cp $PROJ_NAME/settings/local.py.default $PROJ_NAME/settings/local.py
     # for postgres:
     pip install -r requirements/postgre.txt
     # for sqlite:
     pip install -r requirements/sqlite.txt

6. You also need to edit database. Edit file $PROJ_NAME/settings/local.py::

     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.BACKENDHERE!!!',
             'NAME': 'DB_NAME',
             'USER': 'DB_USER',
             'PASSWORD': 'DB_PASSWORD',
             'HOST': 'DB_HOST_OR localhost',
             'PORT': '3306',
             }
     }
7. Settings also need to know where virtualenvironment is located, so edit file $PROJ_NAME/settings.local.py again::
     
     ENV_PATH = proj('.env2.6')
     PYTHON_PATHNAME = 'python2.6'

8. Now you can create database schema::
   make initproject

10. Now project is ready for deployment. Deploy it with nginx+uwsgi or with apache+mod_python
11. When project is running you will need to setup correct site domain.
   a. Open admin interface in browser, it will be available at http://SITE_URL/admin/sites/site/1/. login 'admin@example.com', password 'admin'
   b. Edit and save
12. It is also recommended to change password. It can be done in admin interface too:
   http://SITE_URL/admin/auth/user/1/password/
13. Various project specific settings ccan be changed here:
   http://SITE_URL/settings
   
