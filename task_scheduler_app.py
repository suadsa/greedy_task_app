import streamlit as st

# --- CSS Styling ---
st.markdown("""
    <style>
        body {
            background-color: #f5f5f5;
        }
        .main {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
        }
        .stButton>button {
            background-color: #a2d5c6;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            height: 40px;
        }
        .stButton>button:hover {
            background-color: #6db1a9;
        }
    </style>
""", unsafe_allow_html=True)

class Task:
    def _init_(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.duration))

st.title("Smart Task Organizer")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form"):
    st.subheader("Add a New Task")
    name = st.text_input("Task Name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    submitted = st.form_submit_button("Add Task")
    if submitted and name:
        st.session_state.tasks.append(Task(name, duration, priority))
        st.success("Task added successfully!")

if st.button("Sort Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks")
    total_time = sum(task.duration for task in sorted_tasks)
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task.name}* — {task.duration} mins — Priority: {task.priority}")
    st.info(f"*Total Time:* {total_time} minutes")

if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")

