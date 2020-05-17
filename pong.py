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

# Main game Loop
while True:
    # Update screen
    wn.update()
