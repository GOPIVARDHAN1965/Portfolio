import streamlit as st
from constants import contact

st.title("Contact Me")
st.markdown("---")  # Horizontal divider

# ---- Contact Details ----
st.subheader("Let's Connect!")

st.write("Feel free to reach out to me through any of the following platforms:")

# Display contact links
st.markdown(f"📧 **Email**: [gg23f@fsu.edu](mailto:{contact['email']})")
st.markdown(f"💼 **LinkedIn**: [Visit my LinkedIn Profile]({contact['linkedin']})")
st.markdown(f"🐙 **GitHub**: [Check out my GitHub Repositories]({contact['github']})")

# Optional: Add icons for visual appeal (requires an image or emoji-based approach)
st.write("---")
st.write("Thank you for visiting my portfolio!")