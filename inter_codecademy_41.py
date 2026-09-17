"""
Curso:
Learn Intermediate Python 3 (Codecademy)

Objetivo:
Praticar teste manual: encontrar erro, classificar, corrigir.

Notes:
- teste manual: feito por pessoas
- teste automatizado: feito por código
"""

flight_statuses = {
  903: 'Departed',
  834: 'Boarding',
  359: 'Delayed',
  128: 'On time',
  385: 'On time',
}

print('***Small World Air Flight Information***')
for flight, status in flight_statuses.items():
  #print('Flight ' + flight + ' status: ' + status) #TypeError: int não concatena com str
  print('Flight ' + '903' + ' status: ' + 'Departed')

