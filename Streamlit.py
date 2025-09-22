import streamlit as st

# Page config
st.set_page_config(page_title="Priyadharshini M | Portfolio", page_icon=":computer:")

# --- Header ---
st.markdown(
    """
    <div style="text-align:center">
        <h1 style="color:#5C4033;">Priyadharshini M</h1>
        <p style="color:#5C4033; font-size:18px;">Junior Software Developer | Python | MySQL | HTML | CSS | Excel</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# --- Navigation Buttons ---
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio("", nav, horizontal=True)

st.markdown("---")

# --- About Section ---
if selected == "About":
    st.header("About Me")
    st.write(
        """
        Hello! I'm **Priyadharshini M**, a recent Electronics and Communication Engineering graduate 
        from Karpagam College of Engineering, Coimbatore. I have hands-on experience in Python, MySQL, 
        and web development, with projects in both academic and practical areas. I am passionate about 
        continuous learning and applying my knowledge in real-world applications.
        """
    )

# --- Skills Section ---
elif selected == "Skills":
    st.header("Skills")
    st.write("- Programming: Python")
    st.write("- Database: MySQL")
    st.write("- Web: HTML, CSS")
    st.write("- Tools: VS Code, GitHub, Microsoft Excel")

# --- Projects Section ---
elif selected == "Projects":
    st.header("Projects")
    st.write(
        """
        - **Smart Home Security System** – Designed and implemented a home security system integrating intrusion detection and automation. 
          Utilized sensors and GSM module to enable real-time alerts and notifications on mobile.
        - **Portfolio Website** – A personal website built with HTML and CSS to showcase my profile and projects.
        """
    )

# --- Education Section ---
elif selected == "Education":
    st.header("Education")
    st.write(
        """
        - **B.E. in Electronics and Communication Engineering** (2025)  
          Karpagam College of Engineering, Coimbatore  
          **Percentage:** 75%
        - **Higher Secondary Education (HSC)** – 2021  
          Kalaimagal Kalvi Nilayam Girls Hr Sec School, Erode  
          **Percentage:** 88.28%
        - **Secondary Education (SSLC)** – 2019  
          Carmel Matric Hr Sec School, Erode  
          **Percentage:** 86.6%
        """
    )

# --- Contact Section ---
elif selected == "Contact":
    st.header("Contact")
    st.write("**Email:** priyadharshinim2432@gmail.com")
    st.write("**GitHub:** [github.com/yourgithub](https://github.com/yourgithub)")
    st.write("**LinkedIn:** [linkedin.com/in/priyadharshini2432](https://www.linkedin.com/in/priyadharshini2432)")
    st.write("**Phone:** +91 9790189573")
