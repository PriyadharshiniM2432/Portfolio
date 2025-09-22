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

# Function to set background image with 80% fade
def set_background_image(image_path):
    base64_image = get_base64_image(image_path)
    if base64_image:
        st.markdown(
            f"""
            <style>
            .stApp {{
                background: linear-gradient(
                    rgba(255,255,255,0.8), 
                    rgba(255,255,255,0.8)
                ), url(data:image/jpg;base64,{base64_image});
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                background-attachment: fixed;
                color: #2C2C2C !important;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
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
<div style="text-align:center; background-color: rgba(255,255,255,0.95); 
            padding: 20px; border-radius: 12px; margin-bottom: 20px; 
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
    <h1 style="color:#2C2C2C; margin-bottom:8px;">Priyadharshini M</h1>
    <p style="color:#444; font-size:18px; font-weight:500;">
        Junior Software Developer | Python | MySQL | HTML | CSS | Excel
    </p>
</div>
""", unsafe_allow_html=True)

# Navigation
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

# Remove extra spacing below radio buttons
st.markdown(
    """
    <style>
    /* Remove default padding/margin around radio buttons and main block */
    .stRadio, .css-18e3th9 {
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }
    /* Reduce top padding for main container */
    .css-1d391kg {
        padding-top: 0rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# Set background image if available
if selected in images:
    set_background_image(images[selected])

# Content container CSS
st.markdown("""
<style>
.content-container {
    background-color: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 15px;
    margin: 20px 0;
    box-shadow: 0 6px 12px rgba(0,0,0,0.1);
    color: #2C2C2C;
}
h1, h2, h3, h4, h5, h6, p, li {
    color: #2C2C2C !important;
}
</style>
""", unsafe_allow_html=True)

# Section content
if selected == "About":
    st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("About Me")
    st.write("""
       Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
       from Karpagam College of Engineering, Coimbatore.  
       I have hands-on experience in Python, MySQL, and web development.  
       I am passionate about continuous learning and building real-world applications.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Skills":
    # st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Skills")
    st.write("""
    - **Programming:** Python  
    - **Database:** MySQL  
    - **Web:** HTML, CSS  
    - **Tools:** VS Code, GitHub, Microsoft Excel
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Projects":
    # st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Projects")
    st.write("""
    - **Smart Home Security System** – Designed a security system with sensors + GSM for real-time alerts.  
    - **Portfolio Website** – Built a personal website using HTML and CSS to showcase my work.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Education":
    # st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Education")
    st.write("""
    - **B.E. in Electronics and Communication Engineering** (2025)  
      Karpagam College of Engineering, Coimbatore — **7.95 CGPA**  

    - **Higher Secondary (HSC)** – 2021  
      Kalaimagal Kalvi Nilayam Girls Hr Sec School, Erode — **88.28%**  

    - **Secondary (SSLC)** – 2019  
      Carmel Matric Hr Sec School, Erode — **86.6%**
    """)
    st.markdown('</div>', unsafe_allow_html=True)

elif selected == "Contact":
    # st.markdown('<div class="content-container">', unsafe_allow_html=True)
    st.header("Contact")
    st.write("📧 **Email:** priyadharshinim2432@gmail.com")
    st.write("💻 **GitHub:** [github.com/PriyadharshiniM2432](https://github.com/PriyadharshiniM2432)")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("📱 **Phone:** +91 9790189573")
    st.markdown('</div>', unsafe_allow_html=True)

