import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Максимальный размер под схему без отступов и интерфейса Streamlit
st.set_page_config(page_title="Онтологическая модель", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .block-container {padding: 0rem !important;}
    </style>
""", unsafe_allow_html=True)

# Создаем крупную фигуру для 30+ узлов
fig, ax = plt.subplots(figsize=(18, 11))
G = nx.DiGraph()

# 1. Основные узлы (Состояния, Условия, Действия, Процессы)
# Состояния (Зелёные)
states = ["INIT", "DOWN_1", "RIGHT_1", "UP_1", "LEFT_1", "DOWN_2", "RIGHT_2", "UP_2", "LEFT_2", "DOWN_3", "STOP"]

# Переходы (Голубые)
transitions = [
    "Переход INIT->DOWN_1", "Переход DOWN_1->RIGHT_1", "Переход RIGHT_1->UP_1",
    "Переход UP_1->LEFT_1", "Переход LEFT_1->DOWN_2", "Переход DOWN_2->RIGHT_2",
    "Переход RIGHT_2->UP_2", "Переход UP_2->LEFT_2", "Переход LEFT_2->DOWN_3",
    "Переход DOWN_3->STOP"
]

# Условия (Оранжевые)
conditions = [
    "Условие: Старт", "Условие: y <= -4", "Условие: x >= 4", "Условие: y >= 0",
    "Условие: x <= 1", "Условие: y <= -3", "Условие: x >= 3", "Условие: y >= -1",
    "Условие: x <= 2", "Условие: y <= -2"
]

# Действия разворота (Жёлтые)
actions = ["Разворот вниз (270°)", "Разворот вправо (0°)", "Разворот вверх (90°)", "Разворот влево (180°)"]

# Процесс (Тёмно-синий)
process = "Процесс: Перемещение\n(t.forward)"

# 2. Построение графа и связей с подписями стрелок
edge_labels = {}

# Связи состояний с переходами
G.add_edge("INIT", "Переход INIT->DOWN_1"); edge_labels[("INIT", "Переход INIT->DOWN_1")] = "быть переходом из"
G.add_edge("Переход INIT->DOWN_1", "DOWN_1"); edge_labels[("Переход INIT->DOWN_1", "DOWN_1")] = "переходить в"

G.add_edge("DOWN_1", "Переход DOWN_1->RIGHT_1"); edge_labels[("DOWN_1", "Переход DOWN_1->RIGHT_1")] = "быть переходом из"
G.add_edge("Переход DOWN_1->RIGHT_1", "RIGHT_1"); edge_labels[("Переход DOWN_1->RIGHT_1", "RIGHT_1")] = "переходить в"

G.add_edge("RIGHT_1", "Переход RIGHT_1->UP_1"); edge_labels[("RIGHT_1", "Переход RIGHT_1->UP_1")] = "быть переходом из"
G.add_edge("Переход RIGHT_1->UP_1", "UP_1"); edge_labels[("Переход RIGHT_1->UP_1", "UP_1")] = "переходить в"

G.add_edge("UP_1", "Переход UP_1->LEFT_1"); edge_labels[("UP_1", "Переход UP_1->LEFT_1")] = "быть переходом из"
G.add_edge("Переход UP_1->LEFT_1", "LEFT_1"); edge_labels[("Переход UP_1->LEFT_1", "LEFT_1")] = "переходить в"

G.add_edge("LEFT_1", "Переход LEFT_1->DOWN_2"); edge_labels[("LEFT_1", "Переход LEFT_1->DOWN_2")] = "быть переходом из"
G.add_edge("Переход LEFT_1->DOWN_2", "DOWN_2"); edge_labels[("Переход LEFT_1->DOWN_2", "DOWN_2")] = "переходить в"

G.add_edge("DOWN_2", "Переход DOWN_2->RIGHT_2"); edge_labels[("DOWN_2", "Переход DOWN_2->RIGHT_2")] = "быть переходом из"
G.add_edge("Переход DOWN_2->RIGHT_2", "RIGHT_2"); edge_labels[("Переход DOWN_2->RIGHT_2", "RIGHT_2")] = "переходить в"

G.add_edge("RIGHT_2", "Переход RIGHT_2->UP_2"); edge_labels[("RIGHT_2", "Переход RIGHT_2->UP_2")] = "быть переходом из"
G.add_edge("Переход RIGHT_2->UP_2", "UP_2"); edge_labels[("Переход RIGHT_2->UP_2", "UP_2")] = "переходить в"

G.add_edge("UP_2", "Переход UP_2->LEFT_2"); edge_labels[("UP_2", "Переход UP_2->LEFT_2")] = "быть переходом из"
G.add_edge("Переход UP_2->LEFT_2", "LEFT_2"); edge_labels[("Переход UP_2->LEFT_2", "LEFT_2")] = "переходить в"

G.add_edge("LEFT_2", "Переход LEFT_2->DOWN_3"); edge_labels[("LEFT_2", "Переход LEFT_2->DOWN_3")] = "быть переходом из"
G.add_edge("Переход LEFT_2->DOWN_3", "DOWN_3"); edge_labels[("Переход LEFT_2->DOWN_3", "DOWN_3")] = "переходить в"

G.add_edge("DOWN_3", "Переход DOWN_3->STOP"); edge_labels[("DOWN_3", "Переход DOWN_3->STOP")] = "быть переходом из"
G.add_edge("Переход DOWN_3->STOP", "STOP"); edge_labels[("Переход DOWN_3->STOP", "STOP")] = "переходить в"

# Привязка условий
G.add_edge("Условие: Старт", "Переход INIT->DOWN_1"); edge_labels[("Условие: Старт", "Переход INIT->DOWN_1")] = "быть условием"
G.add_edge("Условие: y <= -4", "Переход DOWN_1->RIGHT_1"); edge_labels[("Условие: y <= -4", "Переход DOWN_1->RIGHT_1")] = "быть условием"
G.add_edge("Условие: x >= 4", "Переход RIGHT_1->UP_1"); edge_labels[("Условие: x >= 4", "Переход RIGHT_1->UP_1")] = "быть условием"
G.add_edge("Условие: y >= 0", "Переход UP_1->LEFT_1"); edge_labels[("Условие: y >= 0", "Переход UP_1->LEFT_1")] = "быть условием"
G.add_edge("Условие: x <= 1", "Переход LEFT_1->DOWN_2"); edge_labels[("Условие: x <= 1", "Переход LEFT_1->DOWN_2")] = "быть условием"
G.add_edge("Условие: y <= -3", "Переход DOWN_2->RIGHT_2"); edge_labels[("Условие: y <= -3", "Переход DOWN_
