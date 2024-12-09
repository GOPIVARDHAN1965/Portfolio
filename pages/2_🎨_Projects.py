import streamlit as st
from constants import projects

st.title("Projects")
st.markdown("---")  # Horizontal divider


for project in projects:
    st.subheader(project["title"])
    st.write(project["description"])
    st.markdown(f"[View on GitHub]({project['link']})")