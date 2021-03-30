import turtle
screen=turtle.Screen()

screen.title('Name the Countries')
image='world_map.gif'

screen.setup(width=800,height=500)
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x,y):
    print(x,y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop() #so that screen doenot exit on click