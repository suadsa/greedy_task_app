!pip install streamlit

import streamlit as st

class Task:
    def _init_(self, name, duration, priority):
        self.name = name
        self.duration = duration
        self.priority = priority

def greedy_schedule(tasks):
    return sorted(tasks, key=lambda x: (x.priority, x.duration))

st.title("منظّم المهام الذكي")
st.write("أدخل مهامك، واختار أولوياتك، وخلينا نرتبها لك!")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

with st.form("task_form"):
    name = st.text_input("اسم المهمة")
    duration = st.number_input("المدة (بالدقائق)", min_value=1, step=1)
    priority = st.selectbox("الأولوية", [1, 2, 3], format_func=lambda x: f"{x} - {'عالية' if x == 1 else 'متوسطة' if x == 2 else 'منخفضة'}")
    submitted = st.form_submit_button("أضف المهمة")
    if submitted:
        st.session_state.tasks.append(Task(name, duration, priority))
        st.success("تمت إضافة المهمة!")

if st.button("رتّب المهام"):
    sorted_tasks = greedy_schedule(st.session_state.tasks)
    st.subheader("المهام المرتبة:")
    for i, task in enumerate(sorted_tasks, 1):
        st.write(f"{i}. *{task.name}* — {task.duration} دقيقة — أولوية: {task.priority}")
