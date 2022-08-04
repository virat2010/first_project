import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## FAKE POP script
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # Create the fake data for that entry
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.ascii_free_email()

        # Create the new user entry
        user = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]

if __name__ == '__main__':
    print("populating users!")
    populate(10)
    print("populating complete!")
