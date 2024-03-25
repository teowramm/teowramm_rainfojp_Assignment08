# main.py
# Name: Mikaela Teowratanakul & Joseph Rainford
# email: teowramm@mail.uc.edu & rainfojp@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date: March 28, 2024
# Course/Section: IS4010-001
# Semester/Year: Spring 2024
# Brief Description of the assignment: This assignment tests our teamwork skills, by having two people work on one single project. This can be accomplished with GitHub and utilizing different packages.

# Brief Description of what this module does. Do not copy/paste from a previous assignment. Put some thought into this: This module imports the connect package and prints some of the results that were obtained from the SQL Query!
# Citations: NA
# Anything else that's relevant: NA

from ConnectPackage.Connect import *

if __name__ == "__main__":
    print("The below stores are in Ohio and their loyalty programs were affected by the fire:")
    for store_id, num_loyalty in storestatusList:
        print ("Store", store_id, "lost", num_loyalty, "customers in the fire")