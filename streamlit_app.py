import turtle

def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)

    if state == "INIT":
        state = "DOWN"
        t.setheading(270)  # Разворот вниз
        return state, turn

    if state == "DOWN":
        t.forward(10)
        # Условие перехода вниз с учетом текущего шага спирали (turn)
        if y <= -4 * turn:
            state = "RIGHT"
            t.setheading(0)  # Разворот вправо
            return state, turn
        return state, turn

    if state == "RIGHT":
        t.forward(10)
        if x >= 4 * turn:
            state = "UP"
            t.setheading(90)  # Разворот вверх
            return state, turn
        return state, turn

    if state == "UP":
        t.forward(10)
        if y >= 4 * (turn - 1):
            state = "LEFT"
            t.setheading(180)  # Разворот влево
            turn += 1  # Увеличиваем радиус витка спирали
            return state, turn
        return state, turn

    if state == "LEFT":
        t.forward(10)
        # Условие завершения спирали на последнем витке
        if x <= -4 * (turn - 1) or (turn > 2 and x <= 2):
            state = "STOP"
            return state, turn
        return state, turn

    return state, turn

def draw():
    start_state = "INIT"
    end_state = "STOP"
    curr_state = start_state

    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)

    t.penup()
    t.goto(0, 0)
    t.pendown()

    turn = 1  длина/радиус витка

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)

    turtle.done()

if __name__ == "__main__":
    draw()
