"""
Course:
Python (Exercism)

Objective:
Develop functions to manage and organize queues at Chaitana's roller coaster.

Notes:
- Métodos alteram a lista original (mutáveis)
- Método append funciona apenas em listas e não posso usar em string
"""


# 1. Add me to the queue
def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    """Add a person to the 'express' or 'normal' queue depending on the ticket number.

    :param express_queue: list - names in the Fast-track queue.
    :param normal_queue: list - names in the normal queue.
    :param ticket_type: int - type of ticket. 1 = express, 0 = normal.
    :param person_name: str - name of person to add to a queue.
    :return: list - the (updated) queue the name was added to.
    """

    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue

# # Teste 1
# express_queue = ["Ana", "Bel", "Bia"]
# normal_queue = ["Jean", "Juju", "Laura"]
# ticket_type = 1
# person_name = "Lari"

# minha_fila = add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name)
# print(minha_fila)


# 2. Where are my friends?
def find_my_friend(queue, friend_name):
    """Search the queue for a name and return their queue position (index).

    :param queue: list - names in the queue.
    :param friend_name: str - name of friend to find.
    :return: int - index at which the friends name was found.
    """

    return queue.index(friend_name)

# # Teste 2
# fila_teste = ["Ale", "Ana", "Bel", "Bia", "Jean", "Juju", "Laura", "Tiago"]
# minha_fila = find_my_friend(fila_teste, "Jean")
# print(minha_fila)


# 3. Can I please join them?
def add_me_with_my_friends(queue, index, person_name):
    """Insert the late arrival's name at a specific index of the queue.

    :param queue: list - names in the queue.
    :param index: int - the index at which to add the new name.
    :param person_name: str - the name to add.
    :return: list - queue updated with new name.
    """

    queue.insert(index, person_name)
    return queue

# # Teste 3
# fila_teste = ["Ale", "Ana", "Bel", "Bia", "Jean", "Juju", "Laura", "Tiago"]
# minha_fila = add_me_with_my_friends(fila_teste, 6, "Lari")
# print(minha_fila)


# 4. Mean person in the queue
def remove_the_mean_person(queue, person_name):
    """Remove the mean person from the queue by the provided name.

    :param queue: list - names in the queue.
    :param person_name: str - name of mean person.
    :return: list - queue update with the mean persons name removed.
    """

    queue.remove(person_name)
    return queue

# # Teste 4
# fila_teste = ["Ale", "Ana", "Bel", "Bia", "Jean", "Juju", "Laura", "Tiago", "Zuzu"]
# minha_fila = remove_the_mean_person(fila_teste, "Zuzu")
# print(minha_fila)


# 5. Namefellows
def how_many_namefellows(queue, person_name):
    """Count how many times the provided name appears in the queue.

    :param queue: list - names in the queue.
    :param person_name: str - name you wish to count or track.
    :return: int - the number of times the name appears in the queue.
    """

    return queue.count(person_name)

# # Teste 5
# fila_teste = ["Ale", "Ana", "Bel", "Bia", "Jean", "Juju", "Laura", "Tiago"]
# minha_fila = how_many_namefellows(fila_teste, "Bel")
# print(minha_fila)


# 6. Remove the last person
def remove_the_last_person(queue):
    """Remove the person in the last index from the queue and return their name.

    :param queue: list - names in the queue.
    :return: str - name that has been removed from the end of the queue.
    """

    return queue.pop()

# # Teste 6
# fila_teste = ["Ale", "Ana", "Bel", "Bia", "Jean", "Juju", "Laura", "Tiago"]
# minha_fila = remove_the_last_person(fila_teste)
# print(minha_fila)


# 7. Sort the Queue List
def sorted_names(queue):
    """Sort the names in the queue in alphabetical order and return the result.

    :param queue: list - names in the queue.
    :return: list - copy of the queue in alphabetical order.
    """

    return sorted(queue)

# # Teste 7
# fila_teste = ["Tiago", "Ana", "Laura", "Ale", "Bia", "Juju", "Bel", "Jean"]
# minha_fila = sorted_names(fila_teste)
# print(minha_fila)
