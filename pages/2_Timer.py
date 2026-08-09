import streamlit as st
import time as t

class Timer:
    def run(self):

        _, timer, _ = st.columns([2, 3, 2])
        timer.title("Study Timer")

        Time_For_Timer = st.number_input(
            "Enter how much time do you want timer to go: ",
            min_value=1,
            max_value=60,
            value=25
        )

        _, col1, col2, col3, _ = st.columns([3, 2, 2, 2, 3])

        start_button = col1.button("START", use_container_width=True)
        stop_button = col2.button("STOP", use_container_width=True)
        reset_button = col3.button("RESET", use_container_width=True)


        if "running" not in st.session_state:
            st.session_state.running = False

        if "start_time" not in st.session_state:
            st.session_state.start_time = 0

        if "remaining_time" not in st.session_state:
            st.session_state.remaining_time = Time_For_Timer * 60


        if start_button:
            st.session_state.running = True
            st.session_state.start_time = t.time()


        if stop_button:
            elapsed_time = t.time() - st.session_state.start_time
            st.session_state.remaining_time -= int(elapsed_time)
            st.session_state.running = False


        if reset_button:
            st.session_state.running = False
            st.session_state.remaining_time = Time_For_Timer * 60


        @st.fragment(run_every=1)
        def timer():

            if st.session_state.running:

                elapsed_time = t.time() - st.session_state.start_time
                remaining = st.session_state.remaining_time - int(elapsed_time)

                if remaining <= 0:
                    remaining = 0
                    st.session_state.running = False

                minutes = remaining // 60
                seconds = remaining % 60

                _, Timer, _ = st.columns([3, 2, 3])
                
                Timer.title(f"{minutes:02d}:{seconds:02d}")

            else:

                minutes = st.session_state.remaining_time // 60
                seconds = st.session_state.remaining_time % 60

                _, Timer, _ = st.columns([3, 2, 3])

                Timer.title(f"{minutes:02d}:{seconds:02d}")


        timer()

timer = Timer()
timer.run()