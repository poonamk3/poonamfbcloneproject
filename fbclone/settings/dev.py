from . base import *
import dj_database_url
import psycopg2
DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fbclonedb',
        'USER': 'postgres',
        'PASSWORD': 'psql',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


db_from_env=dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)
"""

DATABASES = {

    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'daj5avcjro8f4r',
        'USER': 'rzyyczhbuabcsf',
        'PASSWORD': '7bdeea9ad2d24a0dfb9ede4c86f56e47fa0cf842e045c75a9c407f995f193cad',
        'HOST': 'ec2-3-208-79-113.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
"""