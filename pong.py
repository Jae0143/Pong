import turtle

# Create Window
wn = turtle.Screen()

# Title
wn.title("Pong")

# Background color
wn.bgcolor("black")

# Size of the window
wn.setup(width=800, height=600)

# Stops window from refreshing automatically
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
# speed animation (A)
paddle_a.speed(0)
# shape (A)
paddle_a.shape("square")
# Color (A)
paddle_a.color("white")
# No drawing line (A)
paddle_a.penup()
# Set up coordinate (A)
paddle_a.goto(-350, 0)
# Set up size in ratio from 20px by 20px (A)
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

# Paddle B
paddle_b = turtle.Turtle()
# speed animation (B)
paddle_b.speed(0)
# shape (B)
paddle_b.shape("square")
# Color (B)
paddle_b.color("white")
# No drawing line (B)
paddle_b.penup()
# Set up coordinate (A)
paddle_b.goto(350, 0)
# Set up size in ratio from 20px by 20px (B)
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

# ball
ball = turtle.Turtle()
# speed animation (Ball)
ball.speed(0)
# shape (Ball)
ball.shape("square")
# Color (Ball)
ball.color("white")
# No drawing line (Ball)
ball.penup()
# Set up coordinate (Ball)
ball.goto(0, 0)


# Paddle_a movement to up function
def paddle_a_up():
    # get y-coordinate
    y = paddle_a.ycor()
    # add 20 to y coordinate = go up
    y += 20
    # Set new y coordinate
    paddle_a.sety(y)

# Keyboard binding
# Detect keyboard input
wn.listen()
# When user presses w, use function paddle_a_up
wn.onkeypress(paddle_a_up, "w")

# Main game Loop
while True:
    # Update screen
    wn.update()
