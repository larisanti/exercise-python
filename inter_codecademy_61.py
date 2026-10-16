"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar sets.

Notes:
- set = group of elements that are unordered and do not contain duplicates
- pode usar curly braces ou set:
  music = {'pop', 'rock'}
  music = set(['pop', 'rock'])
"""

genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap', 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap', 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin', 'pop', 'pop', 'classical', 'pop', 'country', 'rock', 'classical', 'country', 'pop', 'rap', 'latin']

# Write your code below!
survey_genres = set(genre_results)
print(survey_genres)

survey_abbreviated = {genre[0:3] for genre in genre_results}
print(survey_abbreviated)