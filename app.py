import streamlit as st

st.set_page_config(
    page_title="Matt's Portfolio",
    layout="wide",
    page_icon="media/favicon.svg"
)

# Page definitions
about_page = st.Page("about/about.py", title="About")
solar_remote_sensing_device_page = st.Page("projects/5_solar_sensing_device.py", title="Solar Sensing Device", icon=":material/signal_cellular_alt:")
line_following_robot_page = st.Page("projects/8_line_following_robot.py", title="Line Following Robot", icon=":material/laps:")
dual_axis_solar_tracker_page = st.Page("projects/1_dual_axis_solar_tracker.py", title="Dual Axis Solar Tracker", icon=":material/sunny:")

with st.sidebar:
    st.title("Matt Baughen")
    st.markdown("[MSc Design Engineering](https://google.com) student at [Imperial College London](https://imperial.ac.uk), aiming to specialise in sustainable design")
    st.link_button(label="View my CV 📃", url="https://google.com")

pg = st.navigation(
    {
        "General": [about_page],
        "Projects": [solar_remote_sensing_device_page, line_following_robot_page, dual_axis_solar_tracker_page]
    }
)

st.write("## Hello! My name's Matt")
st.write("I'm an [MSc Design Engineering](https://imperial.ac.uk) student at [Imperial College London](https://google.com), aiming to specialise in sustainable design and the circular economy.")
st.write("This website contains a collection of my favourite industrial and academic projects from the last few years - if you have any questions, please get in touch!")

pg.run()