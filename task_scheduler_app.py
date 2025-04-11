import streamlit as st

# Task class
class Task:
    def _init_(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

# Greedy sorting algorithm with validation
def greedy_schedule(task_dicts):
    valid_tasks = []
    for t in task_dicts:
        try:
            st.write(f"Checking: {repr(t)}")  # For debugging
            if isinstance(t, dict) and all(k in t for k in ['name', 'duration', 'priority']):
                valid_tasks.append(Task(t['name'], t['duration'], t['priority']))
            else:
                st.warning(f"Skipped invalid task: {repr(t)}")
        except Exception as e:
            st.error(f"Error while processing task: {repr(t)} — {e}")
    return sorted(valid_tasks, key=lambda x: (x.priority, x.duration))

# Streamlit UI
st.title("Smart Task Scheduler")
st.write("Add your tasks and we'll help you prioritize them using a greedy approach!")

# Session state for storing tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Task input form
with st.form("task_form"):
    name = st.text_input("Task Name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    submitted = st.form_submit_button("Add Task")
    if submitted:
        st.session_state.tasks.append({
            'name': name,
            'duration': duration,
            'priority': priority
        })
        st.success("Task added successfully!")

# Button to sort tasks
if st.button("Schedule Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks:")
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task.name}* — {task.duration} minutes — Priority: {task.priority}")

