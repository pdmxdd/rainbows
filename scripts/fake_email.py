from random import randint
from faker import Faker

fake = Faker()
# Faker.seed(randint(0, 15000))
email = fake.ascii_free_email()
print(f"{email}")