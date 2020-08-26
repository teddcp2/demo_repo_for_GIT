import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project_level1.settings')

import django
django.setup()

from demoapp1.models import Topic,Webpage,AccessRecord
from faker import Faker
import random

fk=Faker()
nm=['social networking','blogging','travelling','www']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(nm))[0]
    t.save()
    return t

def populate(n=5):
    for i in range(n):
        t=add_topic()

        urlnm=fk.url()
        dt=fk.date()
        nm=fk.company()

        webpg=Webpage.objects.get_or_create(topic=t,name=nm,url=urlnm)[0]
        rcrd=AccessRecord.objects.get_or_create(name=webpg,acessed_date=dt)[0]

        webpg.save()
        rcrd.save()

if __name__=='__main__':
    print('population: started')
    populate(15)
    print('finshed')