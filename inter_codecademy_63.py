"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo
Praticar sets

Notes:
- criar set: {}, set()
- criar frozenset: frozenset()
- adicionar: .add() -> um item, .update() -> vários itens
- remover: .remove() -> erro se não existe, .discard() -> sem erro
- verificar elemento: in
- união: .union() ou |
- interseção: .intersection() ou &
- diferença: .difference() ou -
- diferença simétrica: .symmetric_difference() ou ^
"""

music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])

frozen_tag_union = my_tags | music_tags
print(frozen_tag_union)

regular_tag_intersect = music_tags & my_tags
print(regular_tag_intersect)

frozen_tag_difference = my_tags - music_tags
print(frozen_tag_difference)

regular_tag_sd = music_tags ^ my_tags
print(regular_tag_sd)