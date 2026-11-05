import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

st.set_page_config(page_title="Лабораторная работа №1 — Вариант 1", layout="wide")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. | Группа: ИВТИИбд-14 | Вариант №1 (Спираль)")

# Создаем две вкладки для удобства
tab1, tab2 = st.tabs(["1. Онтологическая модель (Граф)", "2. Траектория спирали (Симуляция)"])

with tab1:
    st.header("Онтологическая модель переходов")
    fig1, ax1 = plt.subplots(figsize=(14, 8))
    G = nx.DiGraph()
    
    states = ["INIT", "DOWN_1", "RIGHT_1", "UP_1", "LEFT_1", "DOWN_2", "RIGHT_2", "UP_2", "LEFT_2", "DOWN_3", "STOP"]
    transitions = [f"Переход {states[i]}->{states[i+1]}" for i in range(len(states)-1)]
    
    for i in range(len(states)-1):
        G.add_edge(states[i], transitions[i])
        G.add_edge(transitions[i], states[i+1])
        
    pos = nx.spring_layout(G, seed=42, k=0.8)
    colors = ['#E53935' if n == "STOP" else ('#0288D1' if "Переход" in n else '#7CB342') for n in G.nodes()]
    
    nx.draw(G, pos, with_labels=True, node_color=colors, node_size=2200, font_size=8, font_color='white', font_weight='bold', ax=ax1, arrows=True)
    st.pyplot(fig1)

with tab2:
    st.header("Графическое отображение траектории робота (Спираль)")
    fig2, ax2 = plt.subplots(figsize=(8, 8))
    
    # Координаты точек спирали для Варианта 1
    px = [0, 0, 100, 100, 25, 25, 75, 75, 50, 50]
    py = [0, -100, -100, 0, 0, -75, -75, -25, -25, -50]
    
    ax2.plot(px, py, marker='o', color='#1E88E5', linewidth=3, markersize=6)
    ax2.set_xlim(-30, 130)
    ax2.set_ylim(-120, 30)
    ax2.axhline(0, color='grey', linewidth=0.8, linestyle='--')
    ax2.axvline(0, color='grey', linewidth=0.8, linestyle='--')
    ax2.grid(True, linestyle=':', alpha=0.6)
    ax2.set_title("Траектория движения (Вариант №1)", fontsize=12, fontweight='bold')
    ax2.set_xlabel("Ось X")
    ax2.set_ylabel("Ось Y")
    
    # Отметка конечной точки STOP
    ax2.annotate('STOP', xy=(50, -50), xytext=(65, -35),
                 arrowprops=dict(facecolor='red', shrink=0.05, width=1.5, headwidth=8),
                 fontsize=11, fontweight='bold', color='red')

    st.pyplot(fig2)
