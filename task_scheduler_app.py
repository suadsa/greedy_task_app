import streamlit as st

# Custom CSS styling
st.markdown("""
    <style>
        /* تغيير الخلفية */
        .stApp {
            background-color: #f0f4f8;
            padding: 20px;
        }
        
        /* تزيين العناوين */
        h1, h2, h3 {
            color: #2e4057;
            font-family: 'Segoe UI', sans-serif;
        }

        /* زر جميل */
        .stButton > button {
            background-color: #a2d5c6;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            height: 40px;
        }

        .stButton > button:hover {
            background-color: #6db1a9;
            color: #ffffff;
        }

        /* مربعات الإدخال */
        .stTextInput, .stNumberInput, .stSelectbox {
            border-radius: 10px;
        }

        /* تخصيص محتوى البطاقة */
        .task-card {
            background-color: #ffffff;
            padding: 10px 15px;
            margin-bottom: 10px;
            border-radius: 10px;
            box-shadow: 1px 1px 8px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# Task class
class Task:
    def _init_(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

# Greedy algorithm
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.duration))

st.title("Smart Task Organizer")

# Session state for tasks
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# Input form
with st.form("task_form"):
    st.subheader("Add a New Task")
    name = st.text_input("Task Name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    submitted = st.form_submit_button("Add Task")
    if submitted and name:
        st.session_state.tasks.append(Task(name, duration, priority))
        st.success("Task added successfully!")

# Sort button
if st.button("Sort Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks")
    total_time = sum(task.duration for task in sorted_tasks)
    for i, task in enumerate(sorted_tasks, 1):
        st.markdown(f"""
            <div class="task-card">
                <strong>{i}. {task.name}</strong><br>
                Duration: {task.duration} mins<br>
                Priority: {task.priority}
            </div>
        """, unsafe_allow_html=True)
    st.info(f"*Total Time:* {total_time} minutes")

# Clear button
if st.button("Clear All Tasks"):
    st.session_state.tasks = []
    st.success("All tasks cleared!")


