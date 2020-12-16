#!/usr/bin/env python3
from connection import Base, engine, session
from classPerson import Person
from classAddresses import Addresses
from classAssociation import Association

Base.metadata.bind = engine
Base.metadata.create_all(engine)
session.add(Person())
session.add(Addresses())
session.add(Association())
session.commit()
Association.__table__.drop()
Person.__table__.drop()
Addresses.__table__.drop()
print("Tables dropped")

Base.metadata.create_all(engine)
#Populate user info
user1 = Person(
	person_name='George',
	person_DOB='1996-6-01',
	active_phone_number='8134441122'
)
user2 = Person(
	person_name='Thomas',
	person_DOB='1969-12-4',
	active_phone_number='9921237744'
)
user3 = Person(
	person_name='Erik',
	person_DOB='1921-11-09',
	active_phone_number='7771234567'
)
user4 = Person(
	person_name='Jack',
	person_DOB='2000-11-25',
	active_phone_number='9002316455'
)

#Populate address info
address1 = Addresses(
	street_address='14th Avenue',
	city='Georgetown',
	state='Alabama',
	zip_code='28301'
)
address2 = Addresses(
	street_address='270 Townstreet',
	city='Tampa',
	state='Florida',
	zip_code='33610'
)
address3 = Addresses(
	street_address='2 Markway',
	city='New-York',
	state='New-York',
	zip_code='12001'
)

# Build associations between addresses and persons
association1 = Association(start_date='2008-03-10', end_date='2010-06-12')
association1.address = address1
user1.addresses.append(association1)

association2 = Association(start_date='2011-05-30')
association2.address = address2
user1.addresses.append(association2)

association3 = Association(start_date='2008-09-10')
association3.address = address3
user2.addresses.append(association3)

association4 = Association(start_date='2000-07-21')
association4.address = address3
user3.addresses.append(association4)

association5 = Association(start_date='2019-12-28')
association5.address = address1
user4.addresses.append(association5)

# Commit changes to tables
session.add(user1)
session.add(user2)
session.add(user3)
session.add(user4)
session.commit()
print("Data populated")
