import streamlit as st

class Task:
    def _init_(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

def greedy_schedule(task_dicts):
    valid_tasks = [
        t for t in task_dicts
        if isinstance(t, dict) and 'name' in t and 'duration' in t and 'priority' in t
    ]
    tasks = [Task(t['name'], t['duration'], t['priority']) for t in valid_tasks]
    sorted_tasks = sorted(tasks, key=lambda x: (x.priority, x.duration))
    return sorted_tasks

st.title("Smart Task Scheduler")
st.write("Enter your tasks and priorities, and let us sort them for you!")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form"):
    name = st.text_input("Task Name")
    duration = st.number_input("Duration (in minutes)", min_value=1, step=1)
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    submitted = st.form_submit_button("Add Task")
    if submitted and name:
        st.session_state.tasks.append({
            'name': name,
            'duration': duration,
            'priority': priority
        })
        st.success("Task added successfully!")

if st.button("Sort Tasks"):
    if st.session_state.tasks:
        sorted_tasks = greedy_schedule(st.session_state.tasks)
        st.subheader("Sorted Tasks:")
        for i, task in enumerate(sorted_tasks, 1):
            st.write(f"{i}. *{task.name}* — {task.duration} min — Priority: {task.priority}")
    else:
        st.warning("No tasks added yet!")

