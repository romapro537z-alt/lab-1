import streamlit as st
import pandas as pd

# Настройка страницы
st.set_page_config(page_title="Лабораторная работа №1", layout="wide")

st.title("Лабораторная работа №1: Моделирование траектории робота")
st.subheader("Студент: Васильченко Р.Д. (группа ИВТИИбд-14) | Вариант №1: Спираль")

# Создаем вкладки для структурирования отчета в приложении
tab1, tab2, tab3 = st.tabs(["1. Онтологическая модель", "2. Условия и Переходы", "3. Генерация кода Python"])

with tab1:
    st.header("Структура онтологии (Состояния и Процессы)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Основные сущности:")
        st.write("• **Начальное состояние:** `INIT`")
        st.write("• **Рабочие состояния:** Вниз 1, Вправо 1, Вверх 1, Влево 1, Вниз 2, Вправо 2, Вверх 2, Влево 2, Вниз 3")
        st.write("• **Конечное состояние:** `STOP` (Остановка)")
        st.write("• **Процесс:** `Движение` (`t.forward(10)`)")
        st.write("• **Действия:** Повороты (`setheading` на 0°, 90°, 180°, 270°)")

    with col2:
        st.markdown("### Граф переходов модели:")
        # Используем встроенный в Streamlit инструмент визуализации графов без внешних библиотек
        st.graphviz_chart('''
            digraph {
                rankdir=LR;
                node [style=filled, fillcolor="#4CAF50", fontcolor=white, fontname="Arial"];
                edge [color="#666666"];
                
                INIT -> "Вниз 1" -> "Вправо 1" -> "Вверх 1" -> "Влево 1" -> "Вниз 2" -> "Вправо 2" -> "Вверх 2" -> "Влево 2" -> "Вниз 3" -> STOP [fillcolor="#F44336"];
            }
        ''')

with tab2:
    st.header("Таблица переходов и геометрических условий (Вариант 1)")
    
    data = {
        "Состояние источника": ["Начальное", "Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3"],
        "Условие перехода": ["Старт", "y <= -4", "x >= 4", "y >= 0", "x <= 1", "y <= -3", "x >= 3", "y >= -1", "x <= 2", "y <= -2"],
        "Целевое состояние": ["Вниз 1", "Вправо 1", "Вверх 1", "Влево 1", "Вниз 2", "Вправо 2", "Вверх 2", "Влево 2", "Вниз 3", "STOP"],
        "Действие (Поворот)": ["t.setheading(270)", "t.setheading(0)", "t.setheading(90)", "t.setheading(180)", "t.setheading(270)", "t.setheading(0)", "t.setheading(90)", "t.setheading(180)", "t.setheading(270)", "Остановка"]
    }
    df = pd.DataFrame(data)
    st.table(df)

with tab3:
    st.header("Автоматически сгенерированный Python-код")
    st.write("Ниже представлен код на языке Python с использованием библиотеки Turtle, полученный на основе построенной онтологии:")
    
    python_code = '''import turtle

def run_turtle_simulation():
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("Моделирование траектории робота - Вариант 1 (Спираль)")
    
    t = turtle.Turtle()
    t.speed(3)
    t.pensize(2)
    
    step_size = 25  # Масштаб витков
    
    # Выполнение переходов и действий по онтологической модели
    t.setheading(270); t.forward(4 * step_size) # Вниз 1
    t.setheading(0);   t.forward(4 * step_size) # Вправо 1
    t.setheading(90);  t.forward(4 * step_size) # Вверх 1
    t.setheading(180); t.forward(3 * step_size) # Влево 1
    t.setheading(270); t.forward(3 * step_size) # Вниз 2
    t.setheading(0);   t.forward(2 * step_size) # Вправо 2
    t.setheading(90);  t.forward(2 * step_size) # Вверх 2
    t.setheading(180); t.forward(1 * step_size) # Влево 2
    t.setheading(270); t.forward(1 * step_size) # Вниз 3 -> STOP
    
    print("Траектория успешно построена. Переход в STOP.")
    screen.mainloop()

if __name__ == "__main__":
    run_turtle_simulation()
'''
    st.code(python_code, language="python")
