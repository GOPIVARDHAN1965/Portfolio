import streamlit as st
from constants import *

st.set_page_config(
    page_title="Portfolio - Introduction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)



# Header Section
st.title(f"Hi, I'm {info['name']}! 👋")

# About Me Section
st.header("About Me")
st.markdown("---") 

# Layout for content
col1, col2 = st.columns([2, 1])  

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
    st.image("static/profile.jpeg", caption=info['name'], use_column_width=True)

# CSS for click-to-zoom effect
st.markdown(
    """
    <style>
    .zoom {
        display: block;
        margin-left: auto;
        margin-right: auto;
        max-width: 300px;
        transition: transform 0.2s ease-in-out; /* Smooth zoom effect */
        cursor: pointer;
    }
    .zoom:hover {
        transform: scale(1.2); /* Zooms in the image on hover */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Skills Section
st.markdown("### My <span style='color:Red'>Skills ⚒️</span>", unsafe_allow_html=True)
st.markdown("---") 

# Skills Tab
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #f4f4f4;
        color: #333;
        border: 1px solid #ddd;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 14px;
        width: 150px; /* Fixed width for uniformity */
        height: 40px; /* Fixed height for uniformity */
        transition: all 0.6s ease; /* Smooth transition for hover effect */
    }

    .stButton button:hover {
        background-color: #28a745; /* Green fill on hover */
        color: white; /* White text on hover */
        transform: scale(1.05); /* Slightly enlarges the button */
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1); /* Adds shadow for 3D effect */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

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
                with col:
                    st.button(next(skill_iter))
            except StopIteration:
                break


with st.spinner("Loading skills..."):
    skill_tab()