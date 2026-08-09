import streamlit as st


class Planner:

    def __init__(self):
        self.Number_Of_Tasks = 0
        self.tasks = []
        self.completed = []
        self.Total_Task = 0
        self.Task_Completed = 0

    def run(self):

        _, planner, _ = st.columns([2, 3, 2])
        planner.title("Study Planner")

        if "Number_Of_Tasks" not in st.session_state:
            st.session_state.Number_Of_Tasks = 0

        Number_Of_Tasks = st.number_input(
            "Enter how many tasks do you want to enter: ",
            min_value=0,
            max_value=7,
            value=st.session_state.Number_Of_Tasks,
            key="number_of_tasks"
        )

        st.session_state.Number_Of_Tasks = Number_Of_Tasks

        if "tasks" not in st.session_state:
            st.session_state.tasks = []

        if "completed" not in st.session_state:
            st.session_state.completed = []

        while len(st.session_state.tasks) < Number_Of_Tasks:
            st.session_state.tasks.append("")

        while len(st.session_state.completed) < Number_Of_Tasks:
            st.session_state.completed.append(False)

        Total_Task = 0
        Task_Completed = 0

        while Total_Task < Number_Of_Tasks:

            Task_Key = f"task_{Total_Task}"
            CheckBox_Key = f"checkbox_{Total_Task}"

            if Task_Key not in st.session_state:
                st.session_state[Task_Key] = st.session_state.tasks[Total_Task]

            Enter_Task = st.text_input(
                "Enter the task you want to complete: ",
                key=Task_Key
            )

            st.session_state.tasks[Total_Task] = Enter_Task

            if CheckBox_Key not in st.session_state:
                st.session_state[CheckBox_Key] = (
                    st.session_state.completed[Total_Task]
                )

            CheckBox_Task = st.checkbox(
                Enter_Task,
                key=CheckBox_Key
            )

            st.session_state.completed[Total_Task] = CheckBox_Task

            if Enter_Task and CheckBox_Task:
                Task_Completed += 1

            Total_Task += 1

        if Number_Of_Tasks > 0:

            Success = (Task_Completed / Number_Of_Tasks) * 100

            st.progress(Task_Completed / Number_Of_Tasks)

            st.write(f"Success: {Success:.2f}%")


planner = Planner()
planner.run()