# Greedy sorting algorithm with validation (fixed)
def greedy_schedule(task_dicts):
    valid_tasks = []
    for t in task_dicts:
        try:
            st.write(f"Checking: {repr(t)}")  # Debug print
            if isinstance(t, dict) and all(k in t for k in ['name', 'duration', 'priority']):
                valid_tasks.append(Task(t['name'], t['duration'], t['priority']))
            else:
                st.warning(f"Skipped invalid task: {repr(t)}")
        except Exception as e:
            st.error(f"Error while processing task: {repr(t)} — {e}")
    return sorted(valid_tasks, key=lambda x: (x.priority, x.duration))
