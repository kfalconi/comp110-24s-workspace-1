"""Draws a scene with random triangular grey mountains, a sunset orange background, a sun, and a green floor."""

__author__ = "730661559"

from turtle import Turtle, colormode, done
import turtle
import random


def main() -> None:
    """The entrypoint of my scene."""
    colormode(255)
    screen = turtle.Screen()
    screen.setup(width=800, height=600)
    t = Turtle()
    draw_sunset_background(t)
    draw_sun(t)
    draw_random_triangular_mountains(t)
    draw_grass_floor(t)
    done()


def draw_sunset_background(t: Turtle) -> None:
    """Draws a sunset orange background."""
    colors = [(255, 111, 0), (255, 143, 0), (255, 160, 0), (255, 179, 0), (255, 193, 7), (255, 213, 79), (255, 224, 130)]
    y = 300
    i = 0
    while i < len(colors):
        color = colors[i]
        t.penup()
        t.goto(-400, y)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        t.goto(400, y)
        t.goto(400, y - 80)  # Adjust the gradient chunk size here
        t.goto(-400, y - 80)  # Adjust the gradient chunk size here
        t.goto(-400, y)
        t.end_fill()
        y -= 80  # Adjust the distance between gradient chunks here
        i += 1


def draw_sun(t: Turtle) -> None:
    """Draws the sun."""
    t.penup()
    t.goto(300, 180)
    t.pendown()
    t.color(254, 217, 5)
    t.begin_fill()
    t.circle(50)
    t.end_fill()


def draw_random_triangular_mountains(t: Turtle) -> None:
    """Draws random triangular grey mountains."""
    colors = [(79, 79, 79), (66, 66, 66)]  # Shades of grey for mountains
    x = -400
    while x < 400:
        t.penup()
        t.goto(x, -200)
        t.pendown()
        height = random.randint(100, 300)
        t.fillcolor(random.choice(colors))
        t.begin_fill()
        t.goto(x + random.randint(50, 150), height)
        t.goto(x + random.randint(200, 300), -200)
        t.goto(x, -200)
        t.end_fill()
        x += random.randint(100, 200)


def draw_grass_floor(t: Turtle) -> None:
    """Draws the green grass floor."""
    t.penup()
    t.goto(-400, -200)
    t.pendown()
    t.color("green")
    t.begin_fill()
    t.goto(400, -200)
    t.goto(400, -300)
    t.goto(-400, -300)
    t.goto(-400, -200)
    t.end_fill()


if __name__ == "__main__":
    main()