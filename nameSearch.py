from classPerson import Person
from connection import session

CONTACTS = session.query(Person)


def printRecord(person):
    # Print record for user.
    print("---------------------------------------")
    print("\n\tName: ", person.person_name)
    print("\tPhone: ", person.active_phone_number)
    print("\n---------------------------------------\n")
    
def displayResults(records):
    if records.count() > 0:
        for person in records:
            printRecord(person)
    else:
        print("\n No Result found")


def exactNameSearch():
	name = input("\n  Enter Exact Name: ")
	
	# SQL to search by exact name
	sql = CONTACTS.filter(Person.person_name.like(name))
	displayResults(sql)


def partialNameSearch():
	name = input("\n  Enter Partial Name: ")
	
	# SQL to search by partial name
	sql = CONTACTS.filter(Person.person_name.like('%{}%'.format(name)))
	displayResults(sql)

