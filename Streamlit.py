import streamlit as st

# Page config
st.set_page_config(page_title="Priyadharshini M | Portfolio", page_icon=":computer:", layout="centered")

# Header
st.markdown("""
<div style="text-align:center">
    <h1 style="color:#5C4033;">Priyadharshini M</h1>
    <p style="color:#5C4033; font-size:18px;">Junior Software Developer | Python | MySQL | HTML | CSS | Excel</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# Navigation
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

st.markdown("---")

# ✅ Use relative paths (works in local + deployment)
images = {
    "About": "img/about.jpg",
    "Skills": "img/skills.jpg",
    "Projects": "img/project.jpg",
    "Education": "img/education.jpg",
    "Contact": "img/contact.jpg"
}

# Display section image
if selected in images:
    st.image(images[selected], use_column_width=True)

# Sections content
if selected == "About":
    st.header("About Me")
    st.write("""
       Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
       from Karpagam College of Engineering, Coimbatore.  
       I have hands-on experience in Python, MySQL, and web development.  
       Passionate about continuous learning and real-world applications.
    """)

elif selected == "Skills":
    st.header("Skills")
    st.write("""
    - Programming: Python  
    - Database: MySQL  
    - Web: HTML, CSS  
    - Tools: VS Code, GitHub, Microsoft Excel
    """)

elif selected == "Projects":
    st.header("Projects")
    st.write("""
    - **Smart Home Security System** – Designed a home security system with sensors + GSM for real-time alerts.  
    - **Portfolio Website** – A personal website built with HTML and CSS to showcase my work.
    """)

elif selected == "Education":
    st.header("Education")
    st.write("""
    - **B.E. in Electronics and Communication Engineering** (2025)  
      Karpagam College of Engineering, Coimbatore — **7.95 CGPA**  

    - **Higher Secondary Education (HSC)** – 2021  
      Kalaimagal Kalvi Nilayam Girls Hr Sec School, Erode — **88.28%**  

    - **Secondary Education (SSLC)** – 2019  
      Carmel Matric Hr Sec School, Erode — **86.6%**
    """)

elif selected == "Contact":
    st.header("Contact")
    st.write("📧 **Email:** priyadharshinim2432@gmail.com")
    st.write("💻 **GitHub:** [github.com/PriyadharshiniM2432](https://github.com/PriyadharshiniM2432)")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("📱 **Phone:** +91 9790189573")
