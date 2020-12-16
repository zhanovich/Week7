#!/usr/bin/env python3
from classAddresses import Addresses
from classAssociation import Association
from ageSearch import ageSearch
from nameSearch import exactNameSearch, partialNameSearch

MENU = '''                                 
1 - Search by Exact Name       
2 - Search by Partial Name           
3 - Search by Age                                               
Q - Quit                       

'''


# Define the main program that will run.
def main():
  # Get user input
  print(MENU)
  menuChoice = input("Menu Selection: ")

  while True:
    #Exact name search
    if menuChoice == "1":
      exactNameSearch()
    #Partial name search
    elif menuChoice == "2":
      partialNameSearch()
    #Age search
    elif menuChoice == "3":
      ageSearch()
    #Exit Application
    elif menuChoice == "Q":
      quit()
    else:
      print("\n\tNot a valid choice. Please select from the menu.\n\n")

    print(MENU)
    menuChoice = input("Menu Selection: ")

main()
