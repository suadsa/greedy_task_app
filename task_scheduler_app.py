import streamlit as st

# ترتيب المهام باستخدام Greedy
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x['priority'], x['duration']))

# تهيئة المهام
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# عنوان التطبيق
st.title("Smart Task Organizer")
st.write("Enter your tasks and we'll schedule them by priority and duration!")

# نموذج المهام
with st.form("task_form"):
    name = st.text_input("Task name", key="task_name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1, key="task_duration")
    priority = st.selectbox(
        "Priority", [1, 2, 3],
        format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}",
        key="task_priority"
    )

    submitted = st.form_submit_button("Add Task")
    if submitted:
        st.session_state.tasks.append({
            'name': st.session_state.task_name,
            'duration': st.session_state.task_duration,
            'priority': st.session_state.task_priority
        })
        st.success("Task added!")

        # تصفير القيم
        st.session_state.task_name = ""
        st.session_state.task_duration = 1
        st.session_state.task_priority = 1

# زر الترتيب
if st.button("Schedule Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks:")
    total_time = 0
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task['name']}* — {task['duration']} min — Priority: {task['priority']}")
        total_time += task['duration']
    st.write(f"*Total time: {total_time} minutes*")
