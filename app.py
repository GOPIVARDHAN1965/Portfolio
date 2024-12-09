import streamlit as st
from constants import *

# Set page configuration
st.set_page_config(
    page_title="Portfolio - Introduction",
    page_icon="🏠",
    layout="wide",
)

# Header Section
st.title(f"Hi, I'm {info['name']}! 👋")

# About Me Section
st.header("About Me")
st.markdown("---")  # Horizontal divider

# Layout for content
col1, col2 = st.columns([2, 1])  # Two-column layout

# Left Column: About Me Text
with col1:
    st.write(info["brief"])
    st.markdown(f"###### 😄 **Name**: {info['name']}")
    st.markdown(f"###### 🎓 **Education**: {education[0]['degree']} at {education[0]['school']}")
    st.markdown(f"###### 📍 **Location**: {info['location']}")
    st.markdown(f"###### 📚 **Interests**: {', '.join(info['fun_facts'])}")

    # Contact Links
    st.markdown(f"###### 👀 **LinkedIn**: [Visit my LinkedIn Profile]({contact['linkedin']})")
    st.markdown(f"###### 🐙 **GitHub**: [Check out my GitHub]({contact['github']})")
    st.markdown(f"###### 🖩 **LeetCode**: [View my LeetCode Profile]({contact['leetcode']})")

    # Resume Download Button
    with open("static/GopiVardhan_Gunta_Resume.pdf", "rb") as file:
        pdf_file = file.read()
    st.download_button(
        label="Download my :blue[Resume]",
        data=pdf_file,
        file_name="Gopi_Vardhan_Gunta_Resume.pdf",
        mime="application/pdf"
    )

# Right Column: Profile Picture
with col2:
    st.image("static/profile.jpeg", width=300, caption=f"{info['name']}")

# Skills Section
st.subheader("My :blue[Skills] ⚒️")
st.markdown("---")  # Horizontal divider

# Skills Tab
def skill_tab():
    rows = len(skills) // skill_col_size
    if len(skills) % skill_col_size != 0:
        rows += 1
    skill_iter = iter(skills)
    for _ in range(rows):
        cols = st.columns(skill_col_size)
        for col in cols:
            try:
                col.button(next(skill_iter))
            except StopIteration:
                break

with st.spinner("Loading skills..."):
    skill_tab()