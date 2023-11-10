from turtle import Turtle
MOVE_STEPS = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    # creating the snake 
    def __init__(self):
        self.Snake = []
        self.create_snake()
        self.head = self.Snake[0]

    def create_snake(self):
        for position in [(0, 0), (-20, 0), (-40, 0)]:
            self.add_segment(position)
            
    def add_segment(self, position):
        # is gonna add segment 
        square = Turtle("square")
        square.color("white")
        square.penup()
        square.goto(position)
        self.Snake.append(square)

    def extend(self):
        self.add_segment(self.Snake[-1].position())


    def move(self):
        # Move the last turtle in the snake to the position of the second-to-last turtle
        # Then move the second-to-last turtle to the position of the third-to-last turtle, etc.
        for i in range(len(self.Snake) - 1, 0, -1):
            new_x = self.Snake[i - 1].xcor()
            new_y = self.Snake[i - 1].ycor()
            self.Snake[i].goto(new_x, new_y)

        # Move the first turtle (head of the snake) forward
        self.head.forward(MOVE_STEPS)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)