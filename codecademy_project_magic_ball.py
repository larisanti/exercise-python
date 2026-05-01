"""
Curso:
Learn Python 3 (Codecademy)

Objetivos:
Praticar if/elif/else e gerar respostas aleatóricas com a biblioteca random.
"""

import random

# Define the name of the user asking the question
name = "Student"

# Define the question to be answered by the Magic 8-Ball
question = "What should I do to improve my English skills?"

# Initialize the variable 'answer' which will hold the randomly selected response
answer = " "

# Generate a random number between 1 and 20
# This number will determine which advice the Magic 8-Ball gives
random_number = random.randint(1, 20)

# Control flow to select the appropriate answer based on the generated random number
if random_number == 1:
    answer = "Read a tongue twister out loud three times."
elif random_number == 2:
    answer = "Record yourself saying the alphabet and listen to it."
elif random_number == 3:
    answer = "Watch the trailer of a movie in English."
elif random_number == 4:
    answer = "Listen to English songs and try to sing them."
elif random_number == 5:
    answer = "Read aloud a paragraph from a book."
elif random_number == 6:
    answer = "Write a comment on social media to practice writing."
elif random_number == 7:
    answer = "Find a podcast about a topic you like."
elif random_number == 8:
    answer = "Try a new language app."
elif random_number == 9:
    answer = "Focus on the intonation and stress patterns in sentences."
elif random_number == 10:
    answer = "Watch a video on YouTube about a topic you like."
elif random_number == 11:
    answer = "Watch live streams in English."
elif random_number == 12:
    answer = "Record yourself saying the lyrics of a song you know."
elif random_number == 13:
    answer = "Read English books or articles that interest you."
elif random_number == 14:
    answer = "Write a short story or journal entry in English."
elif random_number == 15:
    answer = "Practice five new vocabulary words in sentences."
elif random_number == 16:
    answer = "Write a comment online in English."
elif random_number == 17:
    answer = "Learn three new phrasal verbs."
elif random_number == 18:
    answer = "Do five grammar exercises."
elif random_number == 19:
    answer = "Try to think in English during your daily routine."
elif random_number == 20:
    answer = "Speak in English with a friend."
else:
    answer = "Error"  

# Output the user's name, their question, and the Magic 8-Ball's answer
print(name + " asks: " + question)
print("Magic 8-Ball's answer: " + answer)
