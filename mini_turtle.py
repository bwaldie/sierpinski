import turtle
import math
levels = 4

def draw_triangle_c(murtle,triangle_coord_list):
    # routine to draw a triangle
    x=0
    y=1
    a=triangle_coord_list[0]
    b=triangle_coord_list[1]
    c=triangle_coord_list[2]
    
    murtle.penup()
    murtle.fill(True)
    murtle.setposition(a[x],a[y])
    murtle.pendown()
    murtle.setposition(b[x],b[y])
    murtle.setposition(c[x],c[y])
    murtle.setposition(a[x],a[y])
    murtle.penup()
    murtle.fill(False)

def bisect_triangle(triangle_coord_list):
    # triangle_coord_list is the coordinates for a triangle
    # return a list of three triangle vertices
    # [a, b, c] => [a,ab,ac],[ab,b,bc],[ac,bc,c]
    x=0
    y=1
    a = triangle_coord_list[0]
    b = triangle_coord_list[1]
    c = triangle_coord_list[2]
    ab = [(a[x]+b[x])/2,(a[y]+b[y])/2]
    bc = [(b[x]+c[x])/2,(b[y]+c[y])/2]
    ac = [(a[x]+c[x])/2,(a[y]+c[y])/2]
    answer = [[a,ab,ac],[ab,b,bc],[ac,bc,c]]
    return answer
    
def get_triangles(triangle_coord_lists):
    # cycle through the triangles and bisect them
    a = triangle_coord_lists
    bisected_triangle_lists = []
    # levels is defined as a global
    for level in range(levels):
        # clear the list
        bisected_triangle_lists[:] = []
        for triangle in (a):
            b = bisect_triangle(triangle)
            bisected_triangle_lists.extend(b)

        a[:] = []
        a.extend(bisected_triangle_lists)
    return a

def draw_shapes(a):
    # routine to draw a square, circle and triangle
    print("Initializing a drawing window")
    window = turtle.Screen()
    window.bgcolor("white")
    
    print("Creating a turtle for the triangle")
    mick = turtle.Turtle()
    mick.shape("arrow")
    mick.hideturtle()
    mick.pencolor("green")
    mick.fillcolor("blue")
    mick.right(180)
    mick.speed(0)
    # draw the triangles
    for triangle in (a):
        draw_triangle_c(mick,triangle)
        
    window.exitonclick()

def starting_triangle(size):
    # define an equilateral triangle with its center at (0,0)
    # cos(60) = 1/2
    # (x0,y0) = ( -size*sin(60), -size*cos(30))
    # (x1,y1) = (             0,  size*cos(60))
    # (x2,y2) = (  size*sin(60), -size*cos(60))
    return [[-size*math.cos(math.radians(30)),-size*math.sin(math.radians(30))], [0, size*math.cos(math.radians(30))],[ size*math.cos(math.radians(30)),-size*math.sin(math.radians(30))]]
    
   
def main():
    # create a main to limit the variable scope
    triangle_coord_lists = []
    triangle_coord_lists.append(starting_triangle(300))
    draw_shapes(get_triangles(triangle_coord_lists))

main()


