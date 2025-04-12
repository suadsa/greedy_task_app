import streamlit as st
from dataclasses import dataclass

# إعداد الصفحة
st.set_page_config(page_title="Task Scheduler", layout="centered")

# تنسيق مخصص
st.markdown("""
    <style>
        body {
            background-color: #ffeded;
            color: black;
        }

        .stApp {
            background-color: #ffeded;
            color: black;
        }

        .stButton > button {
            background-color: #A2D5C6;
            color: black;
            border: none;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: bold;
        }

        .stForm button {
            background-color: #A2D5C6 !important;
            color: black !important;
            border: none;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: bold;
        }

        .stAlert[data-baseweb="notification"][data-kind="success"] {
            background-color: #B3EACD !important;
            color: black !important;
        }

        .stAlert[data-baseweb="notification"][data-kind="warning"] {
            background-color: #FFD1D1 !important;
            color: black !important;
        }

        .stAlert[data-baseweb="notification"][data-kind="info"] {
            background-color: #D0E8FF !important;
            color: black !important;
        }

        .stTextInput > div > input, .stNumberInput input, .stSelectbox div {
            color: black !important;
            background-color: white !important;
        }
    </style>
""", unsafe_allow_html=True)

# تعريف المهمة
@dataclass
class Task:
    name: str
    duration: int
    priority: int

# الخوارزمية: ترتيب Greedy حسب الأولوية والمدة
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.duration))

# حالة الجلسة لتخزين المهام
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# العنوان
st.title("Smart Task Scheduler")
st.write("Enter your tasks with their duration and priority, and we'll schedule them for you.")

# النموذج لإضافة مهمة
with st.form("task_form"):
    task_name = st.text_input("Task Name")
    task_duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    task_priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    add_button = st.form_submit_button("Add Task")
    if add_button:
        if task_name.strip():
            st.session_state.tasks.append(Task(task_name, task_duration, task_priority))
            st.success("Task added successfully!")
        else:
            st.warning("Please enter a task name.")

# زر ترتيب المهام
if st.button("Sort Tasks"):
    if st.session_state.tasks:
        sorted_tasks = greedy_schedule(st.session_state.tasks)
        st.subheader("Sorted Tasks:")
        total_time = 0
        for i, task in enumerate(sorted_tasks, 1):
            st.write(f"{i}. *{task.name}* — {task.duration} min — Priority: {task.priority}")
            total_time += task.duration
        st.info(f"Total time: {total_time} minutes")
    else:
        st.warning("No tasks to sort.")

# زر لإعادة تعيين القائمة
if st.button("Clear All Tasks"):
    st.session_state.tasks.clear()
    st.success("All tasks cleared!")
