from datetime import date, datetime, timedelta
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

def ageSearch():
    minAge = input("\n  Enter Minimum Age: ")
    maxAge = input("  Enter Maximum Age: ")
    
    # SQL to search by age
    sql = CONTACTS.filter(Person.person_DOB.between(datetime.now() - timedelta(days=int(maxAge) * 365), datetime.now() - timedelta(days=int(minAge) * 365)))
    displayResults(sql)
