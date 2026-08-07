"""
Course:
Python (Exercism)

Objective:
Praticar tratamento de strings e lógica matemática.
"""

def answer(question):
    if question == "What is?":
        raise ValueError("syntax error")
    if question.startswith("What is ") and question.endswith("?"):
        question = question.removeprefix("What is ")
        question = question.removesuffix("?")
        question = question.split()
        parsed = [x for x in question if x != "by"]
        if not parsed:
            raise ValueError("syntax error")

        for idx, item in enumerate(parsed):
            if idx % 2 == 0:
                try:
                    int(item)
                except ValueError:
                    if item in ["plus", "minus", "multiplied", "divided"]:
                        raise ValueError("syntax error")
                    raise ValueError("unknown operation")
            else:
                if item not in ["plus", "minus", "multiplied", "divided"]:
                    is_num = False
                    try:
                        int(item)
                        is_num = True
                    except ValueError:
                        pass
                    
                    if is_num:
                        raise ValueError("syntax error")
                    else:
                        raise ValueError("unknown operation")

        if len(parsed) % 2 == 0:
            raise ValueError("syntax error")

        resultado = int(parsed[0])
        i = 1
        while i < len(parsed):
            operacao = parsed[i]
            next_number = int(parsed[i+1])

            if operacao == "plus":
                resultado += next_number
            elif operacao == "minus":
                resultado -= next_number
            elif operacao == "multiplied":
                resultado *= next_number
            elif operacao == "divided":
                resultado /= next_number
            i += 2
    
        return resultado

    else:
        raise ValueError("unknown operation")

# print(answer("What is 7 minus 5?"))
# print(answer("What is 3 plus 2 multiplied by 3?"))
# print(answer("is 7 minus 5?"))