import streamlit as st

# ترتيب المهام باستخدام خوارزمية Greedy
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x['priority'], x['duration']))

# عنوان التطبيق
st.title("Smart Task Organizer")
st.write("Enter your tasks and we'll schedule them by priority and duration!")

# قائمة المهام في جلسة المستخدم
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# تصفير الحقول بعد الإضافة
if 'name' not in st.session_state:
    st.session_state.name = ""
if 'duration' not in st.session_state:
    st.session_state.duration = 1
if 'priority' not in st.session_state:
    st.session_state.priority = 1

# نموذج إدخال المهام
with st.form("task_form"):
    name = st.text_input("Task name", value=st.session_state.name, key="name_input")
    duration = st.number_input("Duration (in minutes)", min_value=1, step=1, value=st.session_state.duration, key="duration_input")
    priority = st.selectbox("Priority", [1, 2, 3], index=st.session_state.priority - 1, format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}", key="priority_input")
    
    submitted = st.form_submit_button("Add Task")
    if submitted:
        st.session_state.tasks.append({
            'name': name,
            'duration': duration,
            'priority': priority
        })
        st.success("Task added!")

        # نصفر القيم
        st.session_state.name = ""
        st.session_state.duration = 1
        st.session_state.priority = 1

# زر ترتيب المهام
if st.button("Schedule Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks:")
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task['name']}* — {task['duration']} min — Priority: {task['priority']}")
