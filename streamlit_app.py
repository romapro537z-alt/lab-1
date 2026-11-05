import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Убираем все отступы страницы для максимального размера схемы
st.set_page_config(page_title="Схема онтологии", layout="wide", initial_sidebar_state="collapsed")

# Настройка стилей, чтобы убрать лишние элементы Streamlit
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# Создаем граф
fig, ax = plt.subplots(figsize=(14, 8))
G = nx.DiGraph()

# Состояния спирали (Вариант 1)
states = [
    "Начальное", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", 
    "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "Остановка"
]

# Последовательные переходы
for i in range(len(states) - 1):
    G.add_edge(states[i], states[i+1])

# Процесс движения
proc = "Движение\n(t.forward)"
for s in states[1:-1]:
    G.add_edge(s, proc)

# Фиксированная понятная раскладка узлов
pos = nx.planar_layout(G) if nx.is_planar(G) else nx.spring_layout(G, seed=15, k=1.2)

# Цвета
colors = []
for node in G.nodes():
    if node == "Остановка":
        colors.append('#E53935')
    elif "Движение" in node:
        colors.append('#1E88E5')
    else:
        colors.append('#7CB342')

# Отрисовка чистого графа
nx.draw(
    G, pos, with_labels=True, 
    node_color=colors, node_size=3200, 
    font_size=10, font_color='white', font_weight='bold',
    ax=ax, arrows=True, arrowsize=20, edge_color='#555555'
)

# Вывод схемы во весь экран
st.pyplot(fig, use_container_width=True)
