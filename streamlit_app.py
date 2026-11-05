import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Лабораторная работа №1", layout="wide")

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. | Группа: ИВТИИбд-14 | Вариант №1: Спираль")

def get_system_info():
    return {
        "student_name": "Васильченко Роман Дмитриевич",
        "academic_group": "ИВТИИбд-14",
        "variant": "Вариант 1 (Спираль)"
    }

info = get_system_info()
st.sidebar.markdown(f"**Студент:** {info['student_name']}")
st.sidebar.markdown(f"**Группа:** {info['academic_group']}")
st.sidebar.markdown(f"**Вариант:** {info['variant']}")

# Вкладки для интерфейса
tab1, tab2 = st.tabs(["1. Онтологическая модель (Граф)", "2. Логика состояний (Код)"])

with tab1:
    st.header("Граф переходов состояний (Шаблон кафедры)")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    G = nx.DiGraph()
    
    # Цепочка состояний для спирали Варианта 1
    states = [
        "INIT", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", 
        "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "STOP"
    ]
    
    for i in range(len(states) - 1):
        G.add_edge(states[i], states[i+1])
        
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

def perform_switch_case(state, t):
    x = round(t.position()[0] / 20)
    y = round(t.position()[1] / 20)

    if state == "INIT":
        t.setheading(270) # Вниз
        return "DOWN_1"
        
    if state == "DOWN_1":
        t.forward(10)
        if y <= -4:
            t.setheading(0) # Вправо
            return "RIGHT_1"
            
    if state == "RIGHT_1":
        t.forward(10)
        if x >= 4:
            t.setheading(90) # Вверх
            return "UP_1"
            
    if state == "UP_1":
        t.forward(10)
        if y >= 0:
            t.setheading(180) # Влево
            return "LEFT_1"
            
    if state == "LEFT_1":
        t.forward(10)
        if x <= 1:
            t.setheading(270) # Вниз
            return "DOWN_2"
            
    if state == "DOWN_2":
        t.forward(10)
        if y <= -3:
            t.setheading(0) # Вправо
            return "RIGHT_2"
            
    if state == "RIGHT_2":
        t.forward(10)
        if x >= 3:
            t.setheading(90) # Вверх
            return "UP_2"
            
    if state == "UP_2":
        t.forward(10)
        if y >= -1:
            t.setheading(180) # Влево
            return "LEFT_2"
            
    if state == "LEFT_2":
        t.forward(10)
        if x <= 2:
            t.setheading(270) # Вниз (Стоп)
            return "DOWN_3"
            
    if state == "DOWN_3":
        t.forward(10)
        if y <= -2:
            return "STOP"
            
    return state
''', language="python")
