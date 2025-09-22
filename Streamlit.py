import streamlit as st
import base64
import os

# Page config
st.set_page_config(page_title="Priyadharshini M | Portfolio", page_icon=":computer:", layout="centered")

# Function to convert image to base64 for background
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

# Function to set background image
def set_background_image(image_path):
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)), url(data:image/jpg;base64,{base64_image});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# Header
st.markdown("""
<div style="text-align:center; background-color: rgba(255,255,255,0.9); padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h1 style="color:#5C4033;">Priyadharshini M</h1>
    <p style="color:#5C4033; font-size:18px;">Junior Software Developer | Python | MySQL | HTML | CSS | Excel</p>
</div>
""", unsafe_allow_html=True)

# Navigation
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

st.markdown("---")

# Images mapping
images = {
    "About": "img/about.jpg",
    "Skills": "img/skills.jpg",
    "Projects": "img/project.jpg",
    "Education": "img/education.jpg",
    "Contact": "img/contact.jpg"
}

# Set background image based on selected section
if selected in images:
    set_background_image(images[selected])

# Content container with semi-transparent background
content_style = """
<style>
.content-container {
    background-color: rgba(255, 255, 255, 0.9);
    padding: 30px;
    border-radius: 15px;
    margin: 20px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}
</style>
"""
st.markdown(content_style, unsafe_allow_html=True)

# Sections content
if selected == "About":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
       Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
       from Karpagam College of Engineering, Coimbatore.  
       I have hands-on experience in Python, MySQL, and web development.  
       Passionate about continuous learning and real-world applications.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Skills")
    st.write("""
    - Programming: Python  
    - Database: MySQL  
    - Web: HTML, CSS  
    - Tools: VS Code, GitHub, Microsoft Excel
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Projects")
    st.write("""
    - **Smart Home Security System** – Designed a home security system with sensors + GSM for real-time alerts.  
    - **Portfolio Website** – A personal website built with HTML and CSS to showcase my work.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Education":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Education")
    st.write("""
    - **B.E. in Electronics and Communication Engineering** (2025)  
      Karpagam College of Engineering, Coimbatore — **7.95 CGPA**  

    - **Higher Secondary Education (HSC)** – 2021  
      Kalaimagal Kalvi Nilayam Girls Hr Sec School, Erode — **88.28%**  

    - **Secondary Education (SSLC)** – 2019  
      Carmel Matric Hr Sec School, Erode — **86.6%**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Contact":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Contact")
    st.write("📧 **Email:** priyadharshinim2432@gmail.com")
    st.write("💻 **GitHub:** [github.com/PriyadharshiniM2432](https://github.com/PriyadharshiniM2432)")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("📱 **Phone:** +91 9790189573")
    st.markdown('</div>', unsafe_allow_html=True)
