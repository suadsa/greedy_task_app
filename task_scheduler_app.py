import streamlit as st

# تهيئة الجلسة
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# خوارزمية Greedy لترتيب المهام
def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x['priority'], x['duration']))

# واجهة المستخدم
st.title("Smart Task Organizer")
st.write("Enter your tasks and we'll schedule them by priority and duration!")

# نموذج إدخال المهام
with st.form("task_form"):
    name = st.text_input("Task name")
    duration = st.number_input("Duration (minutes)", min_value=1, step=1)
    priority = st.selectbox(
        "Priority",
        [1, 2, 3],
        format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}"
    )
    if st.form_submit_button("Add Task") and name:
        st.session_state.tasks.append({
            'name': name,
            'duration': duration,
            'priority': priority
        })
        st.success("Task added!")

# عرض الأزرار الإضافية
col1, col2 = st.columns(2)
with col1:
    if st.button("Schedule Tasks"):
        if st.session_state.tasks:
            sorted_tasks = greedy_schedule(st.session_state.tasks)
            st.subheader("Sorted Tasks:")
            total_time = sum(t['duration'] for t in sorted_tasks)
            for i, task in enumerate(sorted_tasks, 1):
                st.write(f"{i}. *{task['name']}* — {task['duration']} min — Priority: {task['priority']}")
            st.write(f"*Total time: {total_time} minutes*")
        else:
            st.warning("No tasks to schedule.")

with col2:
    if st.button("Clear All Tasks"):
        st.session_state.tasks = []
        st.success("All tasks cleared.")

# عرض قائمة المهام الحالية (غير مرتبة)
if st.session_state.tasks:
    st.markdown("### Current Tasks")
    for i, t in enumerate(st.session_state.tasks, 1):
        st.write(f"{i}. {t['name']} — {t['duration']} min — Priority: {t['priority']}")
