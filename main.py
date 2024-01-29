#TO DO LIST
#make player controller actually have collisions
#make player controller third person
#add tiling textures
#add more textures
#add a basic UI





from tkinter import *
from ursina import *
from ursina.prefabs.first_person_controller import *
app = Ursina()
window.borderless = False
window.fullscreen = False
def part(Name, Shape, Position, Rotation, Size, Color, Material, Collider):
    Entity(model = Shape,
         position = Position,
         rotation = Rotation,
         scale = Size,
         color = Color,
        texture = Material,
        texture_scale = Size,
           colldier = Collider
           
           
           )
    return

part("Baseplate", "cube", (0,0,0), (0,0,0), (128,10,128), color.rgb(128, 128, 128) , "grass", "box") 
player = part("Player", "cube", (0,10,0), (0,0,0), (1, 5, 4), color.rgb(255, 255, 0), "stud", "box")
EditorCamera()
app.run()



'''
#ill deal with this later
window = Tk()
window.geometry("800x600")
window.title("window!")
icon = PhotoImage(file= "silk icons/src/bricks.png")
window.iconphoto(True, icon)

window.mainloop()
'''
