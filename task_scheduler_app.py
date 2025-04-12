import streamlit as st
from dataclasses import dataclass

# Page configuration
st.set_page_config(page_title="Smart Task Scheduler", page_icon="🗂", layout="centered")

# Custom CSS for soft floral theme
st.markdown(
    """
    <style>
    /* صفحة كاملة بلون وردي فاتح */
    .stApp {
        background-color: #ffeded;
        color: black;
    }
    /* أزرار نعناعي */
    .stButton > button {
        background-color: #A2D5C6;
        color: black;
        border: none;
        border-radius: 10px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton > button:hover {
        background-color: #6DB1A9;
    }
    /* بطاقات المهام */
    .task-card {
        background-color: white;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Task dataclass (for internal use)
@dataclass
class Task:
    name: str
    duration: int
    priority: int

# Greedy scheduling algorithm
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.duration))

# App title and description
st.title("Smart Task Scheduler")
st.write("Enter your tasks and let us prioritize them for you!")

# Initialize session state
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Form to add a task
with st.form("task_form"):
    task_name = st.text_input("Task Name")
    task_duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    task_priority = st.selectbox(
        "Priority",
        [1, 2, 3],
        format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}"
    )
    submitted = st.form_submit_button("Add Task")
    if submitted and task_name:
        st.session_state.tasks.append(Task(task_name, task_duration, task_priority))
        st.success("Task added successfully!")

# Button to sort and display tasks
if st.button("Sort Tasks"):
    if st.session_state.tasks:
        sorted_tasks = greedy_schedule(st.session_state.tasks)
        total_time = sum(t.duration for t in sorted_tasks)
        st.subheader("Sorted Tasks")
        for i, t in enumerate(sorted_tasks, 1):
            st.markdown(f"""
                <div class="task-card">
                    <strong>{i}. {t.name}</strong><br>
                    Duration: {t.duration} minutes<br>
                    Priority: {t.priority}
                </div>
            """, unsafe_allow_html=True)
        st.info(f"*Total time required: {total_time} minutes*")
    else:
        st.warning("No tasks to schedule.")

# Button to clear all tasks
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks have been cleared!")
