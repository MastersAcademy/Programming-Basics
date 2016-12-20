from Admin import Admin
from Subscriber import Subscriber
from faker import Factory as FakerFaktory

faker = FakerFaktory.create()

admin1 = Admin(faker.email(), faker.first_name(), faker.last_name(), 'false', '')
subscriber1 = Subscriber(faker.email(), faker.first_name(), faker.last_name())

print(admin1)
print(subscriber1)

print(admin1.create_user(faker.email()))
