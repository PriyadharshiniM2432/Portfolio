import streamlit as st
import base64

# -----------------------
# Page configuration
# -----------------------
st.set_page_config(
    page_title="Priyadharshini M | Portfolio",
    page_icon=":computer:",
    layout="centered"
)

# -----------------------
# Functions
# -----------------------
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

def set_background_image(image_path):
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: linear-gradient(rgba(255,255,255,0.8), rgba(255,255,255,0.8)),
                            url(data:image/jpg;base64,{base64_image});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #2C2C2C !important;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                text-align: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# -----------------------
# Background images for sections
# -----------------------
images = {
    "About": "img/about.jpg",
    "Skills": "img/skills.jpg",
    "Projects": "img/project.jpg",
    "Education": "img/education.jpg",
    "Contact": "img/contact.jpg"
}

# -----------------------
# Header
# -----------------------
st.markdown("""
<div style="background-color: rgba(255,255,255,0.95); 
            padding: 20px; border-radius: 12px; margin-bottom: 10px; 
            display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h1 style="color:#2C2C2C; margin-bottom:8px;">Priyadharshini M</h1>
    <p style="color:#444; font-size:18px; font-weight:500;">
        Junior Software Developer | Python | MySQL | HTML | CSS | Excel
    </p>
</div>
""", unsafe_allow_html=True)

# -----------------------
# Navigation
# -----------------------
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True, index=0)

# -----------------------
# CSS: Center and style nav buttons
# -----------------------
st.markdown("""
<style>
/* Center radio buttons */
.css-1kyxreq .css-10trblm {justify-content: center !important;}

/* Remove extra spacing below radio buttons */
.css-18e3th9 {margin-bottom:0px !important; padding-bottom:0px !important;}

/* Style radio buttons */
.css-1kyxreq div[role="radiogroup"] label {
    font-size: 20px !important;
    padding: 10px 25px !important;
    color: #2C2C2C !important;
    background-color: #f5e8d0 !important;
    border-radius: 10px;
    margin: 0 5px !important;
    cursor: pointer;
    transition: all 0.2s ease;
}

/* Highlight selected button */
.css-1kyxreq div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) {
    background-color: #d2b48c !important;
    font-weight: bold;
}

/* Hover effect */
.css-1kyxreq div[role="radiogroup"] label:hover {
    background-color: #e0c097 !important;
}

/* Center all text */
h1, h2, h3, h4, h5, h6, p {
    text-align: center !important;
    color: #2C2C2C !important;
}
</style>
""", unsafe_allow_html=True)

# -----------------------
# Horizontal separator
# -----------------------
st.markdown("---")

# -----------------------
# Set background image
# -----------------------
if selected in images:
    set_background_image(images[selected])

# -----------------------
# Section content
# -----------------------
if selected == "About":
    st.header("About Me")
    st.write("""
Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
from Karpagam College of Engineering, Coimbatore.  
I have hands-on experience in Python, MySQL, and web development.  
I am passionate about continuous learning and building real-world applications.
""")

elif selected == "Skills":
    st.header("Skills")
    st.write("""
Programming: Python  
Database: MySQL  
Web: HTML, CSS  
Tools: VS Code, GitHub, Microsoft Excel
""")

elif selected == "Projects":
    st.header("Projects")
    st.write("""
Smart Home Security System – Designed a security system with sensors + GSM for real-time alerts.  
Portfolio Website – Built a personal website using HTML and CSS to showcase my work.
""")

elif selected == "Education":
    st.header("Education")
    st.write("""
B.E. in Electronics and Communication Engineering (2025) – Karpagam College of Engineering, Coimbatore — 7.95 CGPA  

Higher Secondary (HSC) – 2021 – Kalaimagal Kalvi Nilayam Girls Hr Sec School, Erode — 88.28%  

Secondary (SSLC) – 2019 – Carmel Matric Hr Sec School, Erode — 86.6%
""")

elif selected == "Contact":
    st.header("Contact")
    st.write("Email: priyadharshinim2432@gmail.com")
    st.write("GitHub: [github.com/PriyadharshiniM2432](https://github.com/PriyadharshiniM2432)")
    st.write("LinkedIn: [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("Phone: +91 9790189573")
