import streamlit as st
import base64

# Page config
st.set_page_config(
    page_title="Priyadharshini M | Portfolio",
    page_icon=":computer:",
    layout="centered"
)

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

# Map background images to sections
images = {
    "About": "img/about.jpg",
    "Skills": "img/skills.jpg",
    "Projects": "img/project.jpg",
    "Education": "img/education.jpg",
    "Contact": "img/contact.jpg"
}

# Header
st.markdown("""
<div style="background-color: rgba(255,255,255,0.95); 
            padding: 20px; border-radius: 12px; margin-bottom: 20px; 
            display: inline-block; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h1 style="color:#2C2C2C; margin-bottom:8px;">Priyadharshini M</h1>
    <p style="color:#444; font-size:18px; font-weight:500;">
        Junior Software Developer | Python | MySQL | HTML | CSS | Excel
    </p>
</div>
""", unsafe_allow_html=True)

# Custom HTML navbar
nav_html = """
<div style="display:flex; justify-content:center; gap:30px; margin-bottom:10px;">
    <button onclick="window.location.href='#About'" style="padding:10px 20px; border-radius:8px; border:none; background-color:#e0c097; cursor:pointer;">About</button>
    <button onclick="window.location.href='#Skills'" style="padding:10px 20px; border-radius:8px; border:none; background-color:#e0c097; cursor:pointer;">Skills</button>
    <button onclick="window.location.href='#Projects'" style="padding:10px 20px; border-radius:8px; border:none; background-color:#e0c097; cursor:pointer;">Projects</button>
    <button onclick="window.location.href='#Education'" style="padding:10px 20px; border-radius:8px; border:none; background-color:#e0c097; cursor:pointer;">Education</button>
    <button onclick="window.location.href='#Contact'" style="padding:10px 20px; border-radius:8px; border:none; background-color:#e0c097; cursor:pointer;">Contact</button>
</div>
"""

st.markdown(nav_html, unsafe_allow_html=True)
st.markdown("---")

# Set background image
selected = "About"  # default section
if selected in images:
    set_background_image(images[selected])

# Section content (same as before)
st.header("About Me")
st.write("""
Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
from Karpagam College of Engineering, Coimbatore.  
I have hands-on experience in Python, MySQL, and web development.  
I am passionate about continuous learning and building real-world applications.
""")
