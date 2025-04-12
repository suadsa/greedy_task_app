import streamlit as st
from dataclasses import dataclass

Page config

st.set_page_config(page_title="Smart Task Scheduler", page_icon="🧠", layout="centered")

Custom CSS for styling

st.markdown(""" <style> body { background-color: #ffeded; } .stButton > button { background-color: #A5D6C0; color: black; } .task-card { background-color: white; padding: 10px; border-radius: 10px; margin-bottom: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); } </style> """, unsafe_allow_html=True)

Task dataclass

@dataclass class Task: name: str duration: int priority: int

Greedy algorithm to sort tasks

def greedy_schedule(tasks): return sorted(tasks, key=lambda x: (x.priority, x.duration))

App title

st.title("Smart Task Scheduler") st.write("Enter your tasks and let us prioritize them for you!")

Initialize session state

if 'tasks' not in st.session_state: st.session_state.tasks = []

Form for adding a task

with st.form("task_form"): task_name = st.text_input("Task Name") task_duration = st.number_input("Duration (minutes)", min_value=1, step=1) task_priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}") submitted = st.form_submit_button("Add Task") if submitted: st.session_state.tasks.append(Task(task_name, task_duration, task_priority)) st.success("Task added successfully!")

Sort and display tasks

if st.button("Sort Tasks"): sorted_tasks = greedy_schedule(st.session_state.tasks) total_time = sum(task.duration for task in sorted_tasks) st.subheader("Sorted Tasks") for i, task in enumerate(sorted_tasks, 1): st.markdown(f""" <div class="task-card"> <strong>{i}. {task.name}</strong><br> Duration: {task.duration} minutes<br> Priority: {task.priority} </div> """, unsafe_allow_html=True) st.info(f"Total time required: {total_time} minutes")

Clear all tasks

if st.button("Clear All Tasks"): st.session_state.tasks = [] st.success("All tasks have been cleared!")

