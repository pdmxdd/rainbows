from random import randint
from faker import Faker

fake = Faker()
email = fake.ascii_free_email()
print(f"{email}")