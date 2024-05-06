import turtle

def koch_snowflake(turtle, iterations, length):
    if iterations == 0:
        turtle.forward(length)
    else:
        length /= 3.0
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.right(120)
        koch_snowflake(turtle, iterations - 1, length)
        turtle.left(60)
        koch_snowflake(turtle, iterations - 1, length)

def create_snowflake(iterations, length=400):
    window = turtle.Screen()
    window.bgcolor("white")

    snowflake_turtle = turtle.Turtle()
    snowflake_turtle.speed(0)

    for _ in range(3):
        koch_snowflake(snowflake_turtle, iterations, length)
        snowflake_turtle.right(120)

    window.mainloop()

iterations = int(input("Введіть рівень рекурсії для сніжинки: "))
create_snowflake(iterations=iterations)