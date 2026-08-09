import streamlit as st
#python -m streamlit run C:\Users\jhaan\OneDrive\Desktop\StudyFLow\app.py

class StudyFlow:
    def __init__(self):
        self.name = "StudyFlow"
        self.made_by = "Animesh Jha"

    def show_home(self):
        st.title("📚 Welcome to StudyFlow")

        st.write(f"**Made by:** {self.made_by}")

        st.header("Why did I make StudyFlow?")

        st.write(
            "Studying can sometimes be difficult when you have to manage "
            "tasks, stay focused, and keep yourself motivated. "
            "I created StudyFlow to provide simple study tools in one place."
        )

        st.header("Things you can do")

        st.write("📝 **Planner** - Add tasks and track your progress.")
        st.write("⏱️ **Timer** - Use a timer to stay focused while studying.")
        st.write("💡 **Study Tips** - Generate random tips for motivation.")
        st.write("❓ **Random Quiz** - Test yourself with random questions.")
        st.write("📚 **Random Facts** - Learn interesting facts.")

        st.header("Future Plans")

        st.write(
            "I plan to add more study tools, more questions and facts, "
            "better timer features, and more ways to make studying easier."
        )


study_flow = StudyFlow()
study_flow.show_home()