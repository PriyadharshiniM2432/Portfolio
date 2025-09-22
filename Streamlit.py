import streamlit as st
import base64

# =========================
# Page Config
# =========================
st.set_page_config(
    page_title="Priyadharshini M | Portfolio",
    page_icon=":computer:",
    layout="centered"
)

# =========================
# Utility Functions
# =========================
def get_base64_image(image_path):
    """Convert image to base64"""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return None

def set_background_image(image_path):
    """Set background image with overlay"""
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: linear-gradient(
                    rgba(245, 245, 245, 0.95),
                    rgba(245, 245, 245, 0.95)
                ),
                url(data:image/jpg;base64,{base64_image});
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

# =========================
# Custom Styling
# =========================
st.markdown("""
<style>
/* General text */
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    color: #222 !important;
}

/* Headings */
h1, h2, h3, h4 {
    color: #3B2F2F !important;
    font-weight: 600;
}

/* Navigation radio buttons */
div[role=radiogroup] > label {
    background-color: #f0f0f0;
    border-radius: 8px;
    padding: 6px 16px;
    margin: 0 4px;
    cursor: pointer;
    border: 1px solid #ddd;
}
div[role=radiogroup] > label:hover {
    background-color: #e6e6e6;
}
div[role=radiogroup] > label[data-baseweb="radio"]:has(input:checked) {
    background-color: #5C4033 !important;
    color: white !important;
}

/* Content box */
.content-container {
    background-color: white;
    padding: 25px;
    border-radius: 12px;
    margin: 20px 0;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# =========================
# Header
# =========================
st.markdown("""
<div style="text-align:center; background-color:white; padding: 25px; border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.1); margin-bottom: 25px;">
    <h1 style="color:#5C4033; margin-bottom:8px;">Priyadharshini M</h1>
    <p style="color:#444; font-size:18px; margin:0;">Junior Software Developer | Python | MySQL | HTML | CSS | Excel</p>
</div>
""", unsafe_allow_html=True)

# =========================
# Navigation
# =========================
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

st.markdown("---")

# =========================
# Background Images Mapping
# =========================
images = {
    "About": "img/about.jpg",
    "Skills": "img/skills.jpg",
    "Projects": "img/project.jpg",
    "Education": "img/education.jpg",
    "Contact": "img/contact.jpg"
}

if selected in images:
    set_background_image(images[selected])

# =========================
# Content
# =========================
if selected == "About":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
    Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
    from Karpagam College of Engineering, Coimbatore.  
    I have hands-on experience in **Python, MySQL, and Web Development**.  
    I'm passionate about **continuous learning** and applying my skills to real-world projects.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Skills":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Skills")
    st.write("""
    - **Programming:** Python  
    - **Database:** MySQL  
    - **Web Development:** HTML, CSS  
    - **Tools:** VS Code, GitHub, Microsoft Excel
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Projects")
    st.write("""
    - **Smart Home Security System** – Designed a system with sensors + GSM for real-time alerts.  
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
