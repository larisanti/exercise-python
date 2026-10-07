"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objective:
Organize a new classroom using iterables, iterators, and itertools.

Requisites:
- Import and use a student roster (list of dictionaries).
- Create a ClassroomOrganizer class to manage students.
- Implement iterator protocol to iterate student names alphabetically.
- Use itertools to generate all possible seating combinations for tables.
- Filter students by favorite subject and create afterschool program groups.
- Print results to verify combinations and groupings.
"""

import itertools
from roster import student_roster
from classroom_organizer import ClassroomOrganizer

student_roster_iterator = iter(student_roster)
student1 = next(student_roster_iterator)
print(student1)

class ClassroomOrganizer:
  def __init__(self):
    names = [student ["name"] for student in student_roster]
    self.stored_names = sorted(names)

  def get_combinations(self):
    combinations = list(itertools.combinations(self.stored_names, 2))
    return combinations
  
  def get_students_with_subject(self, subject):
    return [student["name"] for student in student_roster if student["favorite_subject"] == subject]

organizer = ClassroomOrganizer()
combinations = organizer.get_combinations()
#print(combinations)

math = organizer.get_students_with_subject("Math")
science = organizer.get_students_with_subject("Science")
mathscience = list(itertools.combinations(list(itertools.chain(math, science)), 4))
print(combinations)

