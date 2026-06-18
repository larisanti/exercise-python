"""
Curso:
Code in Place (Stanford)

Objetivo:
- Criar um haicai (haiku) com a bilioteca call_gpt
"""

from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    
    print("Creating your haiku...")
     
    haiku = call_gpt(f"Write a haiku about '{topic}' that includes the name '{name}'. A haiku has three lines with a 5-7-5 syllable structure.")
    
    response = call_gpt(haiku)
    
    print("\n" + response)

if __name__ == "__main__":
    main()
