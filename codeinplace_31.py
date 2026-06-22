"""
Curso:
Code in Place (Stanford)

Objetivos:
Praticar criação de imagens com a biblioteca Canvas.

Notes:
Entendi que acontece assim:
   1. módulo graphics chama a função create_canvas
   2. função create_canvas cria o objeto com tamanho x por y
   3. variável canvas guarda o objeto
Por isso é possível chamar os métodos diretamente com canvas:
canvas.create_rectangle() -> substituir por outras formas
"""

from graphics import Canvas

def main():
    canvas = graphics.create_canvas(500, 500)

    # Loop to make 10 green squares
    for i in range(10):
        value = i * 10
        
        # Store coordinates in variables
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10
        
        # Create the shape
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'green')
        
        print(i)
        
if __name__ == '__main__':
    main()