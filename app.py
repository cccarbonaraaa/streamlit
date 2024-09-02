import streamlit as st
from PIL import Image

# Set up the main page configuration
st.set_page_config(
    page_title="My Autobiography & Portfolio",
    page_icon=":sparkles:",
    layout="centered"
)

# Custom CSS for navigation menu
st.markdown("""
    <style>
    .menu {
            border-radius: 20px;
            display: flex;
            justify-content: center;
            position: sticky;
            top: 0;
            background-color: #F7B5CA;
            padding: 10px;
            z-index: 1000;
        }
        .menu a {
            color: #921A40;
            font-size: 19px;
            text-decoration: none;
            padding: 10px 10px;
            margin: 0 30px;
            border-radius: 10px;
        }
        .menu a:hover {
            background-color: #C75B7A;
        }
        .section {
            padding: 10px;
            border-bottom: 3px solid #ddd;
            margin-top: 10px;  /* Ensure sections are not hidden behind the sticky menu */
        }   
    }
    </style>
    <div class="menu">
        <a href="#about-me">About Me</a>
        <a href="#projects">Projects</a>
        <a href="#skills">Skills</a>
        <a href="#contact-me">Contact Me</a>
    </div>
""", unsafe_allow_html=True)

# Header
st.title("Welcome to My Portfolio!")
st.markdown("## Hello! I'm Areej Charisse R. Corbete :wave:")

# About Me
st.markdown("<a id='about-me'></a>", unsafe_allow_html=True)
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.header("About Me")
st.subheader("Who Am I?")
st.write("""
    I am a 4th year college student pursuing a Bachelor of Science in Information Technology at Cebu Institute of Technology University. 
    I am passionate about working on innovative projects and learning new technologies.
    A quick learner and adapt easily to new challenges and technologies.
""")

st.subheader("Background")
st.write("""
    I have experience working on various projects in school, primarily focusing on frontend development. 
    While my main expertise is in frontend work, I also have a solid understanding of backend development.
""")

st.subheader("Fun Facts")
st.write("- I am a dancer and an introvert.")
st.write("- I love music and food.")
st.write("- I have a keen interest in photography and visual design.")

# Skills
st.markdown("<a id='skills'></a>", unsafe_allow_html=True)
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.header("Skills")
    
st.subheader("Development Languages")
st.progress(40)
st.write("**Java, Python, JavaScript**")

st.subheader("Front-end Technology")
st.progress(80)
st.write("**HTML, JavaScript, ReactJS**")

st.subheader("Database")
st.progress(60)
st.write("**MySQL**")

st.subheader("Visual Design & Video Editing")
st.progress(90)
st.write("**Proficiency in Canva, Figma, and CapCut**")

# Projects
st.markdown("<a id='projects'></a>", unsafe_allow_html=True)
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.header("Projects")
    
st.subheader("Wildcat's Tracker (01/2023 - 04/2023)")
st.write("Created a tracker prototype using Figma as part of a team.")
    
st.subheader("Internet Voucher System (04/2023 - 07/2023)")
st.write("Developed a system for generating random vouchers for users at an Internet Cafe.")
    
st.subheader("Aerolink Reservation System (06/2023 - 07/2023)")
st.write("Completed a task involving the addition of a passenger to the system.")
    
st.subheader("TimeSpace (07/2023)")
st.write("Developed a mobile application to assist individuals with mental health conditions in finding relief and support.")
    
st.subheader("Bingo Game (09/2023)")
st.write("Created a basic BINGO game using JavaScript within the React.js framework.")
    
st.subheader("Task Queue System (09/2023)")
st.write("Developed a basic task queue system using JavaScript within the React.js framework.")
    

# Contact
st.markdown("<a id='contact-me'></a>", unsafe_allow_html=True)
st.markdown("<div class='section'></div>", unsafe_allow_html=True)
st.header("Contact Me")

st.write("Feel free to reach out if you have any questions!")

st.subheader("Email")
st.write("Primary: [corbetea@mail.com](mailto:orbetea@mail.com)")
st.write("Secondary: [escano.ace19@mail.com](mailto:escano.ace19@mail.com)")
    
st.subheader("Phone")
st.write("09396891215")

st.subheader("GitHub")
st.write("[GitHub Profile](https://github.com/cccarbonaraaa)")


# Footer
st.markdown("---")
st.markdown("© 2024 Areej Charisse R. Corbete | All Rights Reserved")
