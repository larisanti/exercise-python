"""
Course:
Python (Exercism)

Objectives:
Praticar lógica de strings e condicionais.

Notes:
- while + break -> percorrer o índice e parar se atingir a condição
- " ".join(funcao(x) for x in lista) -> transformar cada item da lista, aplicar a função e passar o resultado direto pra outra função
"""

def translate_word(word):
    VOWELS = "aeiou"

    if word[0] in VOWELS or word.startswith("xr") or word.startswith("yt"):
        return word + "ay"

    i = 0
    while i < len(word):
        if word[i:i+2] == "qu":
            i += 2
            break

        if word[i] == "y" and i > 0:
            break

        if word[i] in VOWELS:
            break
            
        # if consonant:
        i += 1
        
    return word[i:] + word[:i] + "ay"

def translate(text):
    return " ".join(translate_word(word) for word in text.split())


#if __name__ == "__main__":
    #print(translate("apple"))
    #print(translate("square"))
    #print(translate("quick fast run"))
