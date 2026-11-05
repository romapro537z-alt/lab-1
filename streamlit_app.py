import streamlit as st
import pandas as pd

st.set_page_config(page_title="Лабораторная работа №1", layout="wide")

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. | Группа: ИВТИИбд-14 | Вариант №1 (Спираль)")

tab1, tab2, tab3 = st.tabs(["1. Онтологическая модель (Граф)", "2. Переходы и Условия", "3. Сгенерированный Python-код"])

with tab1:
    st.header("Интерактивный граф онтологии")
    # Генерируем красивый граф с узлами разного цвета (состояния, условия, процессы)
    st.graphviz_chart('''
        digraph {
            rankdir=LR;
            node [style=filled, fontname="Arial", shape=circle];
            
            // Состояния (Зелёные)
            node [fillcolor="#7CB342", fontcolor=white];
            INIT [label="Начальное"];
            V1 [label="Вниз 1"];
            VP1 [label="Вправо 1"];
            VV1 [label="Вверх 1"];
            VL1 [label="Влево 1"];
            V2 [label="Вниз 2"];
            VP2 [label="Вправо 2"];
            VV2 [label="Вверх 2"];
            VL2 [label="Влево 2"];
            V3 [label="Вниз 3"];
            STOP [label="Остановка", fillcolor="#E53935"];

            // Процесс (Синий)
            node [fillcolor="#1E88E5", shape=box];
            P1 [label="Процесс: Движение (forward)"];

            // Условия и Повороты (Оранжевые)
            node [fillcolor="#FB8C00", shape=ellipse];
            C0 [label="Старт"];
            C1 [label="y <= -4"];
            C2 [label="x >= 4"];
            C3 [label="y >= 0"];
            C4 [label="x <= 1"];
            C5 [label="y <= -3"];
            C6 [label="x >= 3"];
            C7 [label="y >= -1"];
            C8 [label="x <= 2"];
            C9 [label="y <= -2"];

            // Связи
            INIT -> C0 -> V1;
            V1 -> C1 -> VP1;
            VP1 -> C2 -> VV1;
            VV1 -> C3 -> VL1;
            VL1 -> C4 -> V2;
            V2 -> C5 -> VP2;
            VP2 -> C6 -> VV2;
            VV2 -> C7 -> VL2;
            VL2 -> C8 -> V3;
            V3 -> C9 -> STOP;

            V1 -> P1; VP1 -> P1; VV1 -> P1; VL1 -> P1;
            V2 -> P1; VP2 -> P1; VV2 -> P1; VL2 -> P1; V3 -> P1;
        }
    ''')

with tab2:
    st.header("Таблица логики и геометрии переходов")
    df = pd.DataFrame({
        "Из состояния": ["Начальное", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3"],
        "Условие перехода": ["Старт", "y <= -4", "x >= 4", "y >= 0", "x <= 1", "y <= -3", "x >= 3", "y >= -1", "x <= 2", "y <= -2"],
        "В состояние": ["Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "Остановка"],
        "Команда поворота": ["setheading(270)", "setheading(0)", "setheading(90)", "setheading(180)", "setheading(270)", "setheading(0)", "setheading(90)", "setheading(180)", "setheading(270)", "Остановка"]
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
    
    # Витки спирали (Вариант 1)
    t.setheading(270); t.forward(4 * step) # Вниз
    t.setheading(0);   t.forward(4 * step) # Вправо
    t.setheading(90);  t.forward(4 * step) # Вверх
    t.setheading(180); t.forward(3 * step) # Влево
    t.setheading(270); t.forward(3 * step) # Вниз
    t.setheading(0);   t.forward(2 * step) # Вправо
    t.setheading(90);  t.forward(2 * step) # Вверх
    t.setheading(180); t.forward(1 * step) # Влево
    t.setheading(270); t.forward(1 * step) # Вниз (Остановка)
    
    turtle.done()

if __name__ == '__main__':
    draw_spiral()
''', language="python")
