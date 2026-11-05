import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Лабораторная работа №1", layout="wide")

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. | Группа: ИВТИИбд-14 | Вариант №1: Спираль")

# Вкладки для интерфейса
tab1, tab2 = st.tabs(["1. Онтологическая модель (Граф)", "2. Логика состояний (Код)"])

with tab1:
    st.header("Граф переходов состояний")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    G = nx.DiGraph()
    
    states = [
        "INIT", "DOWN", "RIGHT", "UP", "LEFT", "STOP"
    ]
    
    G.add_edges_from([
        ("INIT", "DOWN"),
        ("DOWN", "RIGHT"),
        ("RIGHT", "UP"),
        ("UP", "LEFT"),
        ("LEFT", "DOWN"),
        ("LEFT", "STOP")
    ])
        
    pos = nx.spring_layout(G, seed=42)
    colors = ['#E53935' if n == "STOP" else '#7CB342' for n in G.nodes()]
    
    nx.draw(
        G, pos, with_labels=True, 
        node_color=colors, node_size=2500, 
        font_size=9, font_color='white', font_weight='bold',
        ax=ax, arrows=True, arrowsize=15
    )
    st.pyplot(fig)

with tab2:
    st.header("Исходный код логики (perform_switch_case)")
    st.code('''import turtle

def perform_switch_case(state, t, turn):
    x = round(t.position()[0] / 10)
    y = round(t.position()[1] / 10)

    if state == "INIT":
        state = "DOWN"
        t.setheading(270)
        return state, turn

    if state == "DOWN":
        t.forward(10)
        if y <= -4 * turn:
            state = "RIGHT"
            t.setheading(0)
            return state, turn
        return state, turn

    if state == "RIGHT":
        t.forward(10)
        if x >= 4 * turn:
            state = "UP"
            t.setheading(90)
            return state, turn
        return state, turn

    if state == "UP":
        t.forward(10)
        if y >= 4 * (turn - 1):
            state = "LEFT"
            t.setheading(180)
            turn += 1
            return state, turn
        return state, turn

    if state == "LEFT":
        t.forward(10)
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

    turn = 1  # длина/радиус витка

    while curr_state != end_state:
        curr_state, turn = perform_switch_case(curr_state, t, turn)

    turtle.done()

if __name__ == "__main__":
    draw()
''', language="python")
