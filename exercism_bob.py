"""
Course:
Python (Exercism)

Objective:
Practice string manipulation and conditional logic.

Notes:
- método precisa de parênteses -> isupper(), endswith()
- assinatura da função -> ":"
"""

def response(hey_bob):
    """
    Return Bob's response based on the input text.
    
    Handles questions, shouting, shouting questions, silence, and other speech.
    """

    clean_hey_bob = hey_bob.strip()

    if clean_hey_bob == "":
        return "Fine. Be that way!"
    elif clean_hey_bob.isupper() and clean_hey_bob.endswith("?"):
        return "Calm down, I know what I'm doing!"
    elif clean_hey_bob.endswith("?"):
        return "Sure."
    elif clean_hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."