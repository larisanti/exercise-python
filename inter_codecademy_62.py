"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar sets.

Notes:
- sets não tem índices
^ porque é uma coleção não ordenada
- pra verificar se um elemento está presente -> in
- funciona também pra frozenset
- pra criar set a partir de outra coleção tem que usar set([])
"""

allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])

bad_tags = []
for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)

for tag in bad_tags:
    tag_set.remove(tag)
print(tag_set)

song_data_users['Retro Words'] = tag_set
print(song_data_users)