"""
Course:
Python (Exercism)

Objective:
Transformar cadeia de DNA em cadeia de RNA usando métodos de string.

Notes:
G -> C
C -> G
T -> A
A -> U
"""

def to_rna(dna_strand):
    return dna_strand.translate(str.maketrans("GCTA", "CGAU"))

#print(to_rna("GCTA"))