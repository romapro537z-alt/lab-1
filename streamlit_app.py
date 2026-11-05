import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Убираем все интерфейсные элементы Streamlit, оставляя только чистую схему
st.set_page_config(page_title="Онтологическая модель", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# Создаем холст для подробной схемы
fig, ax = plt.subplots(figsize=(18, 11))
G = nx.DiGraph()

# 1. Узлы модели (30+ штук: состояния, переходы, условия, действия, процесс)
states = ["INIT", "DOWN_1", "RIGHT_1", "UP_1", "LEFT_1", "DOWN_2", "RIGHT_2", "UP_2", "LEFT_2", "DOWN_3", "STOP"]

transitions = [
    "Переход INIT->DOWN_1", "Переход DOWN_1->RIGHT_1", "Переход RIGHT_1->UP_1",
    "Переход UP_1->LEFT_1", "Переход LEFT_1->DOWN_2", "Переход DOWN_2->RIGHT_2",
    "Переход RIGHT_2->UP_2", "Переход UP_2->LEFT_2", "Переход LEFT_2->DOWN_3",
    "Переход DOWN_3->STOP"
]

conditions = [
    "Условие: Старт", "Условие: y <= -4", "Условие: x >= 4", "Условие: y >= 0",
    "Условие: x <= 1", "Условие: y <= -3", "Условие: x >= 3", "Условие: y >= -1",
    "Условие: x <= 2", "Условие: y <= -2"
]

actions = ["Разворот вниз (270°)", "Разворот вправо (0°)", "Разворот вверх (90°)", "Разворот влево (180°)"]
process = "Процесс: Перемещение\n(t.forward)"

edge_labels = {}

# 2. Связи состояний и переходов
pairs = [
    ("INIT", "Переход INIT->DOWN_1", "быть переходом из"),
    ("Переход INIT->DOWN_1", "DOWN_1", "переходить в"),
    ("DOWN_1", "Переход DOWN_1->RIGHT_1", "быть переходом из"),
    ("Переход DOWN_1->RIGHT_1", "RIGHT_1", "переходить в"),
    ("RIGHT_1", "Переход RIGHT_1->UP_1", "быть переходом из"),
    ("Переход RIGHT_1->UP_1", "UP_1", "переходить в"),
    ("UP_1", "Переход UP_1->LEFT_1", "быть переходом из"),
    ("Переход UP_1->LEFT_1", "LEFT_1", "переходить в"),
    ("LEFT_1", "Переход LEFT_1->DOWN_2", "быть переходом из"),
    ("Переход LEFT_1->DOWN_2", "DOWN_2", "переходить в"),
    ("DOWN_2", "Переход DOWN_2->RIGHT_2", "быть переходом из"),
    ("Переход DOWN_2->RIGHT_2", "RIGHT_2", "переходить в"),
    ("RIGHT_2", "Переход RIGHT_2->UP_2", "быть переходом из"),
    ("Переход RIGHT_2->UP_2", "UP_2", "переходить в"),
    ("UP_2", "Переход UP_2->LEFT_2", "быть переходом из"),
    ("Переход UP_2->LEFT_2", "LEFT_2", "переходить в"),
    ("LEFT_2", "Переход LEFT_2->DOWN_3", "быть переходом из"),
    ("Переход LEFT_2->DOWN_3", "DOWN_3", "переходить в"),
    ("DOWN_3", "Переход DOWN_3->STOP", "быть переходом из"),
    ("Переход DOWN_3->STOP", "STOP", "переходить в")
]

for u, v, lbl in pairs:
    G.add_edge(u, v)
    edge_labels[(u, v)] = lbl

# Привязка условий
cond_pairs = [
    ("Условие: Старт", "Переход INIT->DOWN_1"),
    ("Условие: y <= -4", "Переход DOWN_1->RIGHT_1"),
    ("Условие: x >= 4", "Переход RIGHT_1->UP_1"),
    ("Условие: y >= 0", "Переход UP_1->LEFT_1"),
    ("Условие: x <= 1", "Переход LEFT_1->DOWN_2"),
    ("Условие: y <= -3", "Переход DOWN_2->RIGHT_2"),
    ("Условие: x >= 3", "Переход RIGHT_2->UP_2"),
    ("Условие: y >= -1", "Переход UP_2->LEFT_2"),
    ("Условие: x <= 2", "Переход LEFT_2->DOWN_3"),
    ("Условие: y <= -2", "Переход DOWN_3->STOP")
]

for u, v in cond_pairs:
    G.add_edge(u, v)
    edge_labels[(u, v)] = "быть условием"

# Привязка действий (поворотов)
act_pairs = [
    ("Переход INIT->DOWN_1", "Разворот вниз (270°)"),
    ("Переход DOWN_1->RIGHT_1", "Разворот вправо (0°)"),
    ("Переход RIGHT_1->UP_1", "Разворот вверх (90°)"),
    ("Переход UP_1->LEFT_1", "Разворот влево (180°)"),
    ("Переход LEFT_1->DOWN_2", "Разворот вниз (270°)"),
    ("Переход DOWN_2->RIGHT_2", "Разворот вправо (0°)"),
    ("Переход RIGHT_2->UP_2", "Разворот вверх (90°)"),
    ("Переход UP_2->LEFT_2", "Разворот влево (180°)"),
    ("Переход LEFT_2->DOWN_3", "Разворот вниз (270°)")
]

for u, v in act_pairs:
    G.add_edge(u, v)
    edge_labels[(u, v)] = "вызывать"

# Привязка процесса движения
for st_node in states[1:-1]:
    G.add_edge(st_node, process)
    edge_labels[(st_node, process)] = "выполнять в"

# 3. Цветовая схема
color_map = []
for node in G.nodes():
    if node in states:
        color_map.append("#7CB342")  # Зеленый (Состояния)
    elif node in transitions:
        color_map.append("#0288D1")  # Голубой (Переходы)
    elif node in conditions:
        color_map.append("#FF7043")  # Оранжевый (Условия)
    elif node in actions:
        color_map.append("#FBC02D")  # Желтый (Действия)
    else:
        color_map.append("#1A237E")  # Синий (Процесс)

# Генерация позиций и отрисовка графа
pos = nx.spring_layout(G, seed=100, k=0.9)

nx.draw_networkx_nodes(G, pos, node_color=color_map, node_size=1800, ax=ax)
nx.draw_networkx_labels(G, pos, font_size=7, font_color='white', font_weight='bold', ax=ax)
nx.draw_networkx_edges(G, pos, edge_color='#B0BEC5', arrowsize=12, ax=ax)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=5, font_color='#37474F', ax=ax)

ax.axis('off')

# Вывод исключительно онтологической модели во весь экран
st.pyplot(fig, use_container_width=True)
