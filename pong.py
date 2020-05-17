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

# Main game Loop
while True:
    # Update screen
    wn.update()