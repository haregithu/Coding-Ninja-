import turtle

# Define the grid points
GRID_SIZE = 3
POINT_RADIUS = 20
GRID_SPACING = 100
GRID_POINTS = [
    (-GRID_SPACING, GRID_SPACING), (0, GRID_SPACING), (GRID_SPACING, GRID_SPACING),
    (-GRID_SPACING, 0), (0, 0), (GRID_SPACING, 0),
    (-GRID_SPACING, -GRID_SPACING), (0, -GRID_SPACING), (GRID_SPACING, -GRID_SPACING)
]

# Predefined correct pattern (indices of GRID_POINTS)
CORRECT_PATTERN = [0, 4, 8, 2, 6]

# User's drawn pattern
user_pattern = []

# Initialize turtle
screen = turtle.Screen()
screen.title("Pattern Lock")
screen.setup(width=600, height=600)
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.width(2)

def draw_grid():
    """Draw the 3x3 grid of points."""
    pen.penup()
    for point in GRID_POINTS:
        pen.goto(point)
        pen.dot(POINT_RADIUS)

def draw_line(start, end):
    """Draw a line between two points."""
    pen.penup()
    pen.goto(start)
    pen.pendown()
    pen.goto(end)

def check_pattern():
    """Check if the user's pattern matches the correct pattern."""
    if user_pattern == CORRECT_PATTERN:
        print("Unlocked! Pattern is correct.")
    else:
        print("Incorrect pattern. Try again.")

def on_click(x, y):
    """Handle mouse click events."""
    for i, point in enumerate(GRID_POINTS):
        distance = ((x - point[0]) ** 2 + (y - point[1]) ** 2) ** 0.5
        if distance <= POINT_RADIUS:
            if i not in user_pattern:
                user_pattern.append(i)
                if len(user_pattern) > 1:
                    draw_line(GRID_POINTS[user_pattern[-2]], GRID_POINTS[user_pattern[-1]])
                break
    if len(user_pattern) == len(CORRECT_PATTERN):
        check_pattern()
        user_pattern.clear()  # Reset for the next attempt

# Draw the grid
draw_grid()

# Bind the click event
screen.onclick(on_click)

# Start the turtle main loop
turtle.mainloop()
