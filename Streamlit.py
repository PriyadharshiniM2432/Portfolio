# Navigation using st.radio
nav = ["About", "Skills", "Projects", "Education", "Contact"]
selected = st.radio(
    "", nav, horizontal=True, index=0
)

# CSS to center, enlarge, and restyle radio buttons
st.markdown("""
<style>
/* Center radio buttons horizontally */
.css-1kyxreq .css-10trblm {
    justify-content: center !important;
}

/* Remove extra space below radio buttons */
.css-18e3th9 {
    margin-bottom: 0px !important;
    padding-bottom: 0px !important;
}

/* Make buttons bigger with dark letters */
.css-1kyxreq div[role="radiogroup"] label {
    font-size: 20px !important;     /* Bigger text */
    padding: 10px 25px !important;  /* Bigger clickable area */
    color: #2C2C2C !important;      /* Dark text */
    background-color: #f5e8d0 !important; /* Light button background for contrast */
    border-radius: 10px;
    margin: 0 5px !important;
    cursor: pointer;
    transition: all 0.2s ease;
}

/* Highlight selected button */
.css-1kyxreq div[role="radiogroup"] label[data-baseweb="radio"]:has(input:checked) {
    background-color: #d2b48c !important; /* Slightly darker for selected */
    font-weight: bold;
}

/* Change hover color */
.css-1kyxreq div[role="radiogroup"] label:hover {
    background-color: #e0c097 !important;
}
</style>
""", unsafe_allow_html=True)
