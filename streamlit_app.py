import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Лабораторная работа №1", layout="wide")

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. | Группа: ИВТИИбд-14 | Вариант №1 (Спираль)")

tab1, tab2, tab3 = st.tabs(["1. Онтологическая модель", "2. Условия и Переходы", "3. Python-код"])

with tab1:
    st.header("Граф онтологической модели")
    
    # Строим красивый граф в стиле отчётов
    fig, ax = plt.subplots(figsize=(10, 6))
    G = nx.DiGraph()
    
    states = [
        "Начальное", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", 
        "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "Остановка"
    ]
    
    for i in range(len(states) - 1):
        G.add_edge(states[i], states[i+1])
        
    # Добавляем узел процесса перемещения
    proc = "Процесс: Движение\n(t.forward)"
    for s in states[1:-1]:
        G.add_edge(s, proc)

    pos = nx.spring_layout(G, seed=42, k=0.7)
    
    # Раскраска узлов (зелёные - состояния, синий - процесс, красный - стоп)
    colors = []
    for node in G.nodes():
        if node == "Остановка":
            colors.append('#E53935')
        elif "Процесс" in node:
            colors.append('#1E88E5')
        else:
            colors.append('#7CB342')

    nx.draw(
        G, pos, with_labels=True, 
        node_color=colors, node_size=2800, 
        font_size=9, font_color='white', font_weight='bold',
        ax=ax, arrows=True, arrowsize=18
    )
    st.pyplot(fig)

with tab2:
    st.header("Таблица переходов и геометрии")
    df = pd.DataFrame({
        "Источник": ["Начальное", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3"],
        "Условие": ["Старт", "y <= -4", "x >= 4", "y >= 0", "x <= 1", "y <= -3", "x >= 3", "y >= -1", "x <= 2", "y <= -2"],
        "Цель": ["Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "Остановка"],
        "Поворот": ["setheading(270)", "setheading(0)", "setheading(90)", "setheading(180)", "setheading(270)", "setheading(0)", "setheading(90)", "setheading(180)", "setheading(270)", "STOP"]
    })
    st.table(df)

with tab3:
    st.header("Сгенерированный Python-код")
    st.code('''import turtle

def draw_spiral():
    screen = turtle.Screen()
    screen.setup(600, 600)
    t = turtle.Turtle()
    t.speed(3)
    step = 25
    
    t.setheading(270); t.forward(4 * step)
    t.setheading(0);   t.forward(4 * step)
    t.setheading(90);  t.forward(4 * step)
    t.setheading(180); t.forward(3 * step)
    t.setheading(270); t.forward(3 * step)
    t.setheading(0);   t.forward(2 * step)
    t.setheading(90);  t.forward(2 * step)
    t.setheading(180); t.forward(1 * step)
    t.setheading(270); t.forward(1 * step)
    
    turtle.done()

if __name__ == '__main__':
    draw_spiral()
''', language="python")
