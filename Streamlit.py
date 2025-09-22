import streamlit as st

# Page config
st.set_page_config(page_title="Priyadharshini M | Portfolio", page_icon=":computer:", layout="centered")

# --- Custom CSS for styling ---
st.markdown("""
<style>
/* Background image with fade (70% opacity overlay) */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
                url("https://images.unsplash.com/photo-1519389950473-47ba0277781c"); /* replace with your bg */
    background-size: cover;
    background-position: center;
}

/* Dark text */
h1, h2, h3, h4, h5, h6, p, li, span, div {
    color: #222 !important;
}

/* Highlight button style */
div.stButton > button {
    background-color: #8B4513;
    color: white;
    border-radius: 12px;
    padding: 0.6em 1.2em;
    font-weight: bold;
    border: none;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #A0522D;
    color: #fff;
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# --- Header ---
st.markdown("""
<div style="text-align:center">
    <h1>Priyadharshini M</h1>
    <p style="font-size:18px;">Junior Software Developer | Python | MySQL | HTML | CSS | Excel</p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Navigation ---
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

st.markdown("---")

# --- Sections ---
if selected == "About":
    st.header("About Me")
    st.write("""
       Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
       from Karpagam College of Engineering, Coimbatore.  
       I have hands-on experience in Python, MySQL, and web development.  
       Passionate about continuous learning and real-world applications.
    """)
    st.button("Download Resume")

elif selected == "Skills":
    st.header("Skills")
    st.write("""
    - Programming: Python  
    - Database: MySQL  
    - Web: HTML, CSS  
    - Tools: VS Code, GitHub, Microsoft Excel
    """)
    st.button("View GitHub Projects")

elif selected == "Projects":
    st.header("Projects")
    st.write("""
    - **Smart Home Security System** – Designed a home security system with sensors + GSM for real-time alerts.  
    - **Portfolio Website** – A personal website built with HTML and CSS to showcase my work.
    """)
    st.button("See Full Projects")

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
    st.button("Verify Certificates")

elif selected == "Contact":
    st.header("Contact")
    st.write("📧 **Email:** priyadharshinim2432@gmail.com")
    st.write("💻 **GitHub:** [github.com/PriyadharshiniM2432](https://github.com/PriyadharshiniM2432)")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("📱 **Phone:** +91 9790189573")
    st.button("Send Message")
