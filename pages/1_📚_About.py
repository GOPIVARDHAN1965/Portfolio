import streamlit as st
from constants import experience, education

# Title
st.title("About Me")

# ---- Resume Download ----
st.markdown("### Download My Resume")
with open("static/GopiVardhan_Gunta_Resume.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download Resume",
        data=file,
        file_name="GopiVardhan_Gunta_Resume.pdf",
        mime="application/pdf"
    )

# ---- Internships Section ----
st.header("Internships")
for key, internship in experience.items():
    st.subheader(internship["title"])
    st.write(f"**Company**: {internship['company']}")
    st.write(f"**Duration**: {internship['duration']}")
    st.write(internship["details"])

# ---- Education Section ----
st.header("Education")
for edu in education:
    st.subheader(edu["degree"])
    st.write(f"{edu['school']}, {edu['year']}")
    st.write(edu["details"])