from tkinter import *
from entity_class import *

root = Tk()

image_01 = PhotoImage(file = "image/floor.png")
image_02 = PhotoImage(file = "image/wall.png")
hero_down = PhotoImage(file = "image/hero-down.png")
hero_up = PhotoImage(file = "image/hero-up.png")
hero_right = PhotoImage(file = "image/hero-right.png")
hero_left = PhotoImage(file = "image/hero-left.png")
map_name = "map.txt"
canvas = Canvas(root, width = 700, height = 770, bg = "white")
canvas.pack()


class Entity(object):
    def __init__(self, X = 35, Y = 35):
        self.X = X
        self.Y = Y

    def move(self, dx, dy):
        canvas.move(self.hero_imag, dx, dy)

    def draw_entity(self, X = 35, Y = 35, entity_image = hero_down):
        self.hero_imag = canvas.create_image(self.X, self.Y, image = entity_image)

    
class Hero(Entity):
    def __init__(self, X = 35, Y = 35):
        super().__init__(X, Y)



def import_walls_to_list(file_name):
    try:
        with open(file_name, "r") as f:
            line_list = f.read().splitlines()
            return line_list
    except Exception:
        print("File read error!")


def draw_tiles():
    wall_list = import_walls_to_list(map_name)
    distance = 70
    for i, line in enumerate(wall_list):
        for j, value in enumerate(line):
            if str(value) == "0":
                image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_01)
            elif str(value) == "1":
                image_floor = canvas.create_image(35+j*distance, 35+i*distance, image = image_02)



def on_key_press(e):
    if ( e.keysym == 'Up' ):
        hero.move(0,-70)
    elif( e.keysym == 'Down' ):
        hero.move(0,70)
    elif( e.keysym == 'Right'):
        hero.move(70,0)
    elif ( e.keysym == 'Left'):
        hero.move(-70,0)
        

draw_tiles()
hero = Hero()
hero.draw_entity()
root.bind("<KeyPress>", on_key_press)


root.mainloop()
