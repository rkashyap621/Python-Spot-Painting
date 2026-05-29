import colorgram
import turtle as t
import random

def extract_colors(image, number_of_colors,):
    extracted_colors = colorgram.extract(image, number_of_colors)
    extracted_rgb_tuples=[]
    for k in range(len(extracted_colors)):
        color = extracted_colors[k].rgb
        color_rgb_values = (color.r, color.g, color.b)
        extracted_rgb_tuples.append(color_rgb_values)
    return extracted_rgb_tuples

def spot_paint(file_name, num_colors, num_spots, num_lines, spot_size,spot_dist):
    colors=extract_colors(file_name, num_colors)

    t.colormode(255)
    screen=t.Screen()
    screen.canvheight=spot_size*2*num_lines
    screen.canvwidth=spot_size*num_spots*spot_dist
    screen.setup(screen.canvwidth,screen.canvheight)

    bob=t.Turtle()
    bob.shape("turtle")
    bob.hideturtle()
    bob.penup()
    bob.setpos(-1*(screen.canvwidth/2),-1*(screen.canvheight/2)+spot_size)
    current_pos = bob.pos()

    for i in range(num_lines):
        for j in range(num_spots):
            bob.dot(spot_size,random.choice(colors))
            bob.forward(spot_dist)
        bob.setpos(current_pos[0],current_pos[1]+spot_dist)
        current_pos = bob.pos()
