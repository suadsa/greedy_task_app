import streamlit as st

# تعريف المهمة كـ Dictionary وليس كـ كائن من كلاس
# لأن Streamlit ما يحفظ الكائنات المخصصة مثل Task بشكل صحيح بين الجلسات

def greedy_schedule(tasks):
    # نرتب المهام حسب الأولوية (أقل رقم = أولوية أعلى) ثم حسب المدة
    return sorted(tasks, key=lambda x: (x['priority'], x['duration']))

# واجهة المستخدم
st.title("Smart Task Organizer")
st.write("Enter your tasks and we'll schedule them by priority and duration!")

# التأكد من وجود قائمة المهام في جلسة Streamlit
if 'tasks' not in st.session_state:
    st.session_state.tasks = []

# نموذج إدخال المهام
with st.form("task_form"):
    name = st.text_input("Task name")
    duration = st.number_input("Duration (in minutes)", min_value=1, step=1)
    priority = st.selectbox("Priority", [1, 2, 3], format_func=lambda x: f"{x} - {'High' if x == 1 else 'Medium' if x == 2 else 'Low'}")
    submitted = st.form_submit_button("Add Task")
    if submitted:
        st.session_state.tasks.append({
            'name': name,
            'duration': duration,
            'priority': priority
        })
        st.success("Task added!")

# زر لعرض وترتيب المهام
if st.button("Schedule Tasks"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("Sorted Tasks:")
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task['name']}* — {task['duration']} min — Priority: {task['priority']}")
